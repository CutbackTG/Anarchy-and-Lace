from django.shortcuts import render, get_object_or_404, redirect
from .decorators import staff_required
from catalog.models import Product
from catalog.forms import ProductForm


@staff_required
def dashboard(request):
    product_count = Product.objects.count()
    low_stock = Product.objects.filter(stock_qty__lte=2)

    context = {
        "product_count": product_count,
        "low_stock": low_stock,
    }
    return render(request, "manager/dashboard.html", context)


@staff_required
def product_list(request):
    products = Product.objects.all().order_by("-created_at")
    return render(request, "manager/product_list.html", {"products": products})


@staff_required
def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("manager:product_list")
    else:
        form = ProductForm()

    return render(request, "manager/product_form.html", {"form": form})


@staff_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("manager:product_list")
    else:
        form = ProductForm(instance=product)

    return render(request, "manager/product_form.html", {"form": form, "product": product})


@staff_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        product.delete()
        return redirect("manager:product_list")

    return render(request, "manager/product_confirm_delete.html", {"product": product})
