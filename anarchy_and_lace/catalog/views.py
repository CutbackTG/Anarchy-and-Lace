from django.shortcuts import render, get_object_or_404
from .models import Product, Collection


def product_list(request):
    products = Product.objects.filter(is_active=True)
    collections = Collection.objects.all()

    collection_slug = request.GET.get("collection")
    if collection_slug:
        products = products.filter(collections__slug=collection_slug)

    context = {
        "products": products,
        "collections": collections,
        "current_collection": collection_slug,
    }
    return render(request, "catalog/product_list.html", context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    context = {"product": product}
    return render(request, "catalog/product_detail.html", context)
