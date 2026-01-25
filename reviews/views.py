from django.shortcuts import render, get_object_or_404
from .models import Review
from catalog.models import Product
from django.http import HttpResponseRedirect
from django.urls import reverse

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    reviews = product.reviews.all()

    if request.method == 'POST':
        text = request.POST.get('text')
        rating = int(request.POST.get('rating'))
        Review.objects.create(
            product=product,
            user=request.user,
            text=text,
            rating=rating
        )
        return HttpResponseRedirect(reverse('product_detail', args=[product_id]))

    return render(request, 'product_detail.html', {'product': product, 'reviews': reviews})
