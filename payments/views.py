from __future__ import annotations

from decimal import Decimal

import stripe
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST

from catalog.models import Product
from orders.models import Order, OrderItem


def _cart(session) -> dict[str, int]:
    cart = session.get("cart")
    if not isinstance(cart, dict):
        cart = {}
        session["cart"] = cart
    return cart


@require_POST
def create_checkout_session(request):
    cart = _cart(request.session)

    if not cart:
        messages.error(request, "Your cart is empty.")
        return redirect("cart:cart")

    if not settings.STRIPE_SECRET_KEY:
        messages.error(request, "Stripe isn't configured (missing STRIPE_SECRET_KEY).")
        return redirect("cart:cart")

    # Parse product IDs safely
    ids: list[int] = []
    for pid in cart.keys():
        try:
            ids.append(int(pid))
        except (TypeError, ValueError):
            continue

    products = Product.objects.filter(id__in=ids)
    product_map = {p.id: p for p in products}

    # Build Stripe line items + prepare OrderItems
    line_items: list[dict] = []
    prepared_items: list[dict] = []
    subtotal = Decimal("0.00")

    for pid_str, qty in cart.items():
        try:
            pid = int(pid_str)
            qty_int = int(qty)
        except (TypeError, ValueError):
            continue

        if qty_int <= 0:
            continue

        p = product_map.get(pid)
        if not p:
            continue

        price = p.price or Decimal("0.00")
        unit_amount = int(price * 100)  # pence
        if unit_amount <= 0:
            continue

        qty_int = min(qty_int, 99)
        subtotal += price * qty_int

        line_items.append(
            {
                "price_data": {
                    "currency": "gbp",
                    "product_data": {"name": p.name},
                    "unit_amount": unit_amount,
                },
                "quantity": qty_int,
            }
        )

        prepared_items.append(
            {
                "product": p,
                "product_name": p.name,
                "sku": getattr(p, "sku", "") or "",
                "unit_price": price,
                "quantity": qty_int,
            }
        )

    if not line_items:
        messages.error(request, "Your cart has no valid items.")
        return redirect("cart:cart")

    # ✅ Create a PENDING Order before redirecting to Stripe
    order = Order.objects.create(
        user=request.user if request.user.is_authenticated else None,
        email=request.user.email if request.user.is_authenticated else "",
        status=Order.Status.PENDING,
        currency="GBP",
        subtotal=subtotal,
        total=subtotal,  # webhook will update total with shipping
    )

    for it in prepared_items:
        OrderItem.objects.create(
            order=order,
            product=it["product"],
            product_name=it["product_name"],
            sku=it["sku"],
            unit_price=it["unit_price"],
            quantity=it["quantity"],
        )

    stripe.api_key = settings.STRIPE_SECRET_KEY

    success_url = request.build_absolute_uri(reverse("payments:success"))
    cancel_url = request.build_absolute_uri(reverse("payments:cancel"))

    # Preferred: shipping rates created in Stripe dashboard (shr_...)
    shipping_options: list[dict] = []
    standard_rate = getattr(settings, "STRIPE_SHIPPING_RATE_STANDARD", "")
    tracked_rate = getattr(settings, "STRIPE_SHIPPING_RATE_TRACKED24", "")

    if standard_rate:
        shipping_options.append({"shipping_rate": standard_rate})
    if tracked_rate:
        shipping_options.append({"shipping_rate": tracked_rate})

    # Fallback: define rates inline (works without Stripe dashboard setup)
    if not shipping_options:
        shipping_options = [
            {
                "shipping_rate_data": {
                    "type": "fixed_amount",
                    "fixed_amount": {"amount": 0, "currency": "gbp"},
                    "display_name": "Free shipping",
                    "delivery_estimate": {
                        "minimum": {"unit": "business_day", "value": 3},
                        "maximum": {"unit": "business_day", "value": 5},
                    },
                }
            },
            {
                "shipping_rate_data": {
                    "type": "fixed_amount",
                    "fixed_amount": {"amount": 495, "currency": "gbp"},
                    "display_name": "Tracked 24",
                    "delivery_estimate": {
                        "minimum": {"unit": "business_day", "value": 1},
                        "maximum": {"unit": "business_day", "value": 2},
                    },
                }
            },
        ]

    stripe_session = stripe.checkout.Session.create(
        mode="payment",
        line_items=line_items,
        customer_email=request.user.email if request.user.is_authenticated else None,
        phone_number_collection={"enabled": True},
        billing_address_collection="required",
        shipping_address_collection={"allowed_countries": ["GB"]},
        shipping_options=shipping_options,
        success_url=success_url + "?session_id={CHECKOUT_SESSION_ID}",
        cancel_url=cancel_url,
        # ✅ critical: link Stripe checkout to our Order for webhook handling
        metadata={"order_id": str(order.id)},
    )

    # Save Stripe session reference on the order
    order.stripe_checkout_session_id = stripe_session.id
    order.save(update_fields=["stripe_checkout_session_id"])

    # Store pending session id so we can validate the success return
    request.session["pending_checkout_session_id"] = stripe_session.id
    request.session.modified = True

    return redirect(stripe_session.url, code=303)


def success(request):
    """
    User returns here after Stripe Checkout.
    We verify the checkout session with Stripe, then:
      - clear cart ONLY if payment is confirmed paid
      - show an order complete message + order number if available
    """
    session_id = request.GET.get("session_id")
    pending_id = request.session.get("pending_checkout_session_id")

    context = {
        "verified": False,
        "order": None,
        "order_ref": None,
        "email": None,
        "amount_total": None,
        "currency": None,
    }

    if not session_id:
        messages.warning(request, "Missing checkout session. If you paid, your order is still processing.")
        return render(request, "payments/success.html", context)

    if not pending_id or session_id != pending_id:
        messages.warning(
            request,
            "We couldn't verify this checkout against your current session. "
            "If you completed payment, your order is still processing."
        )
        return render(request, "payments/success.html", context)

    if not settings.STRIPE_SECRET_KEY:
        messages.warning(request, "Stripe isn't configured. We can't verify payment right now.")
        return render(request, "payments/success.html", context)

    stripe.api_key = settings.STRIPE_SECRET_KEY

    try:
        stripe_session = stripe.checkout.Session.retrieve(session_id)
    except Exception:
        messages.warning(request, "We couldn't confirm payment yet. If you paid, your order is still processing.")
        return render(request, "payments/success.html", context)

    payment_status = getattr(stripe_session, "payment_status", None)

    # Try to fetch the order using metadata.order_id
    metadata = getattr(stripe_session, "metadata", {}) or {}
    order_id = metadata.get("order_id")
    if order_id:
        context["order"] = Order.objects.filter(id=order_id).first()

    if payment_status == "paid":
        # UX: clear cart + pending id. Webhook is still the source of truth for DB status.
        request.session["cart"] = {}
        request.session.pop("pending_checkout_session_id", None)
        request.session.modified = True

        amount_total = getattr(stripe_session, "amount_total", None)
        currency = getattr(stripe_session, "currency", None)

        order = context["order"]
        order_ref = order.order_number if order else stripe_session.id

        context.update(
            {
                "verified": True,
                "order_ref": order_ref,
                "email": getattr(stripe_session, "customer_details", {}).get("email", None)
                if isinstance(getattr(stripe_session, "customer_details", None), dict)
                else getattr(getattr(stripe_session, "customer_details", None), "email", None),
                "amount_total": (amount_total / 100) if amount_total else None,
                "currency": (currency.upper() if currency else None),
            }
        )

        messages.success(request, f"Order complete! Reference: {order_ref}")
    else:
        messages.info(request, "Payment not fully confirmed yet. If you paid, your order is still processing.")

    return render(request, "payments/success.html", context)


def cancel(request):
    return render(request, "payments/cancel.html")
