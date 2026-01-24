from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Exists, OuterRef
from django.shortcuts import get_object_or_404, redirect, render

from catalog.models import Product
from orders.models import Order, OrderItem
from .forms import ReviewForm
from .models import Review


def _user_has_purchased(user, product) -> bool:
    return OrderItem.objects.filter(
        order__user=user,
        order__status=Order.Status.PAID,
        product=product,
    ).exists()


@login_required
def create_or_update_review(request, product_id: int):
    product = get_object_or_404(Product, id=product_id)

    if not _user_has_purchased(request.user, product):
        messages.error(request, "You can only review items you’ve purchased.")
        return redirect("catalog:product_detail", product.id)

    review = Review.objects.filter(product=product, user=request.user).first()

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            r = form.save(commit=False)
            r.product = product
            r.user = request.user
            r.save()
            messages.success(request, "Review saved. Thank you!")
            return redirect("catalog:product_detail", product.id)
    else:
        form = ReviewForm(instance=review)

    return render(request, "reviews/review_form.html", {"product": product, "form": form, "review": review})
