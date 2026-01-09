from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def cart_view(request):
    """
    Minimal cart page placeholder.
    Later: wire session cart / DB cart items here.
    """
    return render(request, "cart/cart.html")
