from __future__ import annotations

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from catalog.models import Product
from orders.models import Order
from .forms import ReviewForm
from .models import Review


@login_required
def add_review_from_order(request, order_number: str, product_id: int):
    """
    Create or edit a review for a product that the user purchased in this order.
    """
    order = get_object_or_404(Order, order_number=order_number, user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    # Ensure this product is actually in the order
    if not order.items.filter(product_id=product_id).exists():
        messages.error(request, "You can only review items you’ve purchased.")
        return redirect("orders:order_detail", order_number=order_number)

    # If they already reviewed this product, edit that review instead of creating a duplicate
    existing_review = Review.objects.filter(user=request.user, product_id=product_id).first()

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=existing_review)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.featured = False  # users can't self-feature
            review.save()

            messages.success(request, "Thanks! Your review has been saved.")
            return redirect("orders:order_detail", order_number=order_number)
    else:
        form = ReviewForm(instance=existing_review)

    return render(
        request,
        "reviews/review_form.html",
        {
            "form": form,
            "order": order,
            "product": product,
            "existing_review": existing_review,
        },
    )
