from __future__ import annotations

from decimal import Decimal

import stripe
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST

from catalog.models import Product


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

    line_items = []
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

        line_items.append(
            {
                "price_data": {
                    "currency": "gbp",
                    "product_data": {"name": p.name},
                    "unit_amount": unit_amount,
                },
                "quantity": min(qty_int, 99),
            }
        )

    if not line_items:
        messages.error(request, "Your cart has no valid items.")
        return redirect("cart:cart")

    stripe.api_key = settings.STRIPE_SECRET_KEY

    success_url = request.build_absolute_uri(reverse("payments:success"))
    cancel_url = request.build_absolute_uri(reverse("payments:cancel"))

    # Preferred: shipping rates created in Stripe dashboard (shr_...)
    shipping_options = []
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

        metadata={"cart_items": str(len(cart))},
    )

    return redirect(stripe_session.url, code=303)


def success(request):
    return render(request, "payments/success.html")


def cancel(request):
    return render(request, "payments/cancel.html")
