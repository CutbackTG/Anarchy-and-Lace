# cart/views.py
from __future__ import annotations

from decimal import Decimal

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from catalog.models import Product


def _get_cart(session) -> dict[str, int]:
    cart = session.get("cart")
    if not isinstance(cart, dict):
        cart = {}
        session["cart"] = cart
    return cart


def cart_view(request):
    cart = _get_cart(request.session)

    # Build a cleaned cart that only contains valid product IDs still in the DB
    cleaned_cart: dict[str, int] = {}
    product_ids: list[int] = []

    for pid_str, qty in cart.items():
        try:
            pid = int(pid_str)
            qty_int = int(qty)
        except (TypeError, ValueError):
            continue

        if qty_int <= 0:
            continue

        cleaned_cart[str(pid)] = qty_int
        product_ids.append(pid)

    # Fetch products that actually exist
    products = Product.objects.filter(id__in=product_ids)
    product_map = {p.id: p for p in products}

    items = []
    subtotal = Decimal("0.00")

    # Only keep products that exist
    final_cart: dict[str, int] = {}

    for pid_str, qty_int in cleaned_cart.items():
        pid = int(pid_str)
        product = product_map.get(pid)
        if not product:
            continue

        line_total = (product.price or Decimal("0.00")) * qty_int
        subtotal += line_total

        items.append({"product": product, "qty": qty_int, "line_total": line_total})
        final_cart[pid_str] = qty_int

    # If we dropped anything, write the cleaned version back into the session
    if final_cart != cart:
        request.session["cart"] = final_cart
        request.session.modified = True

    context = {
        "items": items,
        "subtotal": subtotal,
        # IMPORTANT: count only real items
        "cart_count": sum(i["qty"] for i in items),
    }
    return render(request, "cart/cart.html", context)


@require_POST
def cart_add(request, product_id: int):
    product = get_object_or_404(Product, id=product_id)

    cart = _get_cart(request.session)
    key = str(product.id)

    cart[key] = int(cart.get(key, 0)) + 1
    request.session.modified = True

    messages.success(request, f"Added {product.name} to your cart.")

    next_url = request.POST.get("next") or request.META.get("HTTP_REFERER")
    if next_url:
        return redirect(next_url)

    return redirect("cart:cart")


@require_POST
def cart_remove(request, product_id: int):
    cart = _get_cart(request.session)
    key = str(product_id)

    if key in cart:
        del cart[key]
        request.session.modified = True
        messages.success(request, "Removed item from your cart.")

    return redirect("cart:cart")


@require_POST
def cart_set_qty(request, product_id: int):
    cart = _get_cart(request.session)
    key = str(product_id)

    try:
        qty = int(request.POST.get("qty", "1"))
    except (TypeError, ValueError):
        qty = 1

    if qty <= 0:
        cart.pop(key, None)
        messages.success(request, "Item removed.")
    else:
        cart[key] = min(qty, 99)
        messages.success(request, "Cart updated.")

    request.session.modified = True
    return redirect("cart:cart")


@require_POST
def cart_clear(request):
    request.session["cart"] = {}
    request.session.modified = True
    messages.success(request, "Cart cleared.")
    return redirect("cart:cart")
