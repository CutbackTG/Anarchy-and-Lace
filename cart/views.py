from __future__ import annotations

from decimal import Decimal

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from catalog.models import Product


def _get_cart(session) -> dict[str, int]:
    """
    Cart stored in session as:
    session["cart"] = { "<product_id>": quantity, ... }
    """
    cart = session.get("cart")
    if not isinstance(cart, dict):
        cart = {}
        session["cart"] = cart
    return cart


def _cart_count(cart: dict[str, int]) -> int:
    return sum(int(qty) for qty in cart.values() if qty)


def cart_view(request):
    cart = _get_cart(request.session)

    product_ids = [int(pid) for pid in cart.keys()] if cart else []
    products = Product.objects.filter(id__in=product_ids)

    # Keep stable ordering like the session keys
    product_map = {p.id: p for p in products}

    items = []
    subtotal = Decimal("0.00")

    for pid_str, qty in cart.items():
        pid = int(pid_str)
        product = product_map.get(pid)
        if not product:
            continue

        qty = int(qty)
        line_total = (product.price or Decimal("0.00")) * qty
        subtotal += line_total

        items.append(
            {
                "product": product,
                "qty": qty,
                "line_total": line_total,
            }
        )

    context = {
        "items": items,
        "subtotal": subtotal,
        "cart_count": _cart_count(cart),
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

    # Redirect back to where the user came from (product page), fallback to cart
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
    """
    Sets quantity from a POST field named 'qty'.
    qty <= 0 removes the item.
    """
    cart = _get_cart(request.session)
    key = str(product_id)

    try:
        qty = int(request.POST.get("qty", "1"))
    except ValueError:
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
