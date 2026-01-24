from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from .models import Order


@login_required
def my_orders(request):
    orders = (
        Order.objects.filter(user=request.user)
        .order_by("-created_at")
        .prefetch_related("items")
    )
    return render(request, "orders/my_orders.html", {"orders": orders})


@login_required
def order_detail(request, order_number: str):
    order = get_object_or_404(
        Order.objects.prefetch_related("items"),
        user=request.user,
        order_number=order_number,
    )
    return render(request, "orders/order_detail.html", {"order": order})
