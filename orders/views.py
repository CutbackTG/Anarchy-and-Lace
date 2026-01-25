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

import logging
logger = logging.getLogger(__name__)

def product_detail(request, product_slug):
    try:
        # Your normal product detail code here
        product = Product.objects.get(slug=product_slug)
        return render(request, 'product_detail.html', {'product': product})
    except Exception as e:
        logger.exception("Error rendering product detail for %s", product_slug)
        raise e  # Re-raise the exception after logging
