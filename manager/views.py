from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from catalog.models import Product, ProductImage
from .decorators import staff_required
from .forms import ProductForm


@staff_required
@require_POST
def product_image_delete(request, product_id, image_id):
    product = get_object_or_404(Product, pk=product_id)
    image = get_object_or_404(ProductImage, pk=image_id, product=product)

    image.delete()
    messages.success(request, "Image deleted.")
    return redirect("manager:product_edit", pk=product.pk)


class StaffOnlyAuthenticationForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        super().confirm_login_allowed(user)
        if not user.is_staff:
            raise PermissionDenied("Staff access only.")


class ManagerLoginView(LoginView):
    template_name = "manager/login.html"
    authentication_form = StaffOnlyAuthenticationForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return "/manager/"


@staff_required
def dashboard(request):
    product_count = Product.objects.count()
    low_stock = Product.objects.filter(stock_qty__lte=2)

    return render(request, "manager/dashboard.html", {
        "product_count": product_count,
        "low_stock": low_stock,
    })


@staff_required
def product_list(request):
    products = Product.objects.all().order_by("-created_at")
    return render(request, "manager/product_list.html", {"products": products})


@staff_required
def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            messages.success(request, "Product created.")
            return redirect("manager:product_edit", pk=product.pk)
    else:
        form = ProductForm()

    return render(request, "manager/product_form.html", {
        "form": form,
        "mode": "create",
    })


@staff_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)

        # handle image upload separately
        if "image" in request.FILES:
            ProductImage.objects.create(
                product=product,
                image=request.FILES["image"]
            )

        if form.is_valid():
            form.save()
            messages.success(request, "Product updated.")
            return redirect("manager:product_edit", pk=product.pk)
    else:
        form = ProductForm(instance=product)

    return render(request, "manager/product_form.html", {
        "form": form,
        "product": product,
        "mode": "edit",
    })


@staff_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        product.delete()
        messages.success(request, "Product deleted.")
        return redirect("manager:product_list")

    return render(request, "manager/product_confirm_delete.html", {"product": product})
