from __future__ import annotations

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from catalog.models import Product
from orders.models import OrderItem
from .forms import ReviewForm
from .models import Review
from django.contrib import messages
from orders.models import Order


@login_required
def add_review_from_order(request, order_number: str, product_id: int):
    """
    Allow a user to leave a review/testimonial for a product they purchased in a given order.
    """
    order = get_object_or_404(Order, order_number=order_number, user=request.user)

    # Ensure this product is actually in the order
    has_product = order.items.filter(product_id=product_id).exists()
    if not has_product:
        messages.error(request, "You can only review items you’ve purchased.")
        return redirect("orders:order_detail", order_number=order_number)

    # Prevent duplicate reviews for same user + same product (optional but recommended)
    if Review.objects.filter(user=request.user, product_id=product_id).exists():
        messages.info(request, "You’ve already left a review for this item.")
        return redirect("orders:order_detail", order_number=order_number)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product_id = product_id
            review.featured = False  # users cannot set featured
            review.save()

            messages.success(request, "Thank you! Your testimonial has been added.")
            return redirect("orders:order_detail", order_number=order_number)
    else:
        form = ReviewForm()

    return render(request, "reviews/review_form.html", {"form": form, "order": order})
