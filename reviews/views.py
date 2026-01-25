from __future__ import annotations

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from catalog.models import Product
from orders.models import OrderItem
from .forms import ReviewForm
from .models import Review


@login_required
def review_product(request, product_id: int):
    """
    Create or edit a review for a product.

    Rules:
    - User must be logged in
    - User must have purchased the product
    - One review per user per product
    """
    product = get_object_or_404(Product, id=product_id)

    # Only allow reviews if user bought this product
    has_bought = OrderItem.objects.filter(
        order__user=request.user,
        order__status__in=["paid", "complete"],
        product_id=product_id,
    ).exists()

    if not has_bought:
        return redirect("catalog:product_detail", slug=product.slug)

    # One review per user per product (edit if exists)
    review = Review.objects.filter(product=product, user=request.user).first()

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.product = product
            obj.user = request.user
            obj.save()
            return redirect("catalog:product_detail", slug=product.slug)
    else:
        form = ReviewForm(instance=review)

    return render(request, "reviews/review_form.html", {"product": product, "form": form})
