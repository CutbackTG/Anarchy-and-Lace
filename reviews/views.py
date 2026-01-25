from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from catalog.models import Product
from .forms import ReviewForm
from .models import Review


@login_required
def review_product(request, product_id: int):
    product = get_object_or_404(Product, id=product_id)

    # One review per user per product (edit if exists)
    review = Review.objects.filter(product=product, user=request.user).first()

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.product = product
            obj.user = request.user
            obj.save()
            return redirect("catalog:product_detail", slug=product.id)
    else:
        form = ReviewForm(instance=review)

    return render(request, "reviews/review_form.html", {"product": product, "form": form})
