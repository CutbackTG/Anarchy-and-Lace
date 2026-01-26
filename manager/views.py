from __future__ import annotations

from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST

from catalog.models import Product, ProductImage
from orders.models import Order
from .decorators import staff_required
from .forms import ProductForm


# ----------------------------
# Auth
# ----------------------------
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
        return reverse("manager:dashboard")


# ----------------------------
# Dashboard
# ----------------------------
@staff_required
def dashboard(request):
    product_count = Product.objects.count()
    low_stock = Product.objects.filter(stock_qty__lte=2)
    order_count = Order.objects.count()
    pending_orders = Order.objects.filter(status="Pending")

    return render(request, "manager/dashboard.html", {
        "product_count": product_count,
        "low_stock": low_stock,
        "order_count": order_count,
        "pending_orders": pending_orders,
        "active_menu_item": "dashboard",
    })



# ----------------------------
# Products
# ----------------------------
@staff_required
def product_list(request):
    products = Product.objects.all().order_by("-created_at")
    return render(
        request,
        "manager/product_list.html",
        {
            "products": products,
            "active_menu_item": "product_list",
        },
    )


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

    return render(
        request,
        "manager/product_form.html",
        {
            "form": form,
            "mode": "create",
            "active_menu_item": "product_create",
        },
    )


@staff_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)

        # Save product fields first
        if form.is_valid():
            form.save()

            # Optional image upload
            if "image" in request.FILES:
                try:
                    ProductImage.objects.create(product=product, image=request.FILES["image"])
                    messages.success(request, "Product updated and image uploaded.")
                except Exception as e:
                    messages.error(request, f"Product updated, but image upload failed: {e}")
            else:
                messages.success(request, "Product updated.")

            return redirect("manager:product_edit", pk=product.pk)

    else:
        form = ProductForm(instance=product)

    return render(
        request,
        "manager/product_form.html",
        {
            "form": form,
            "product": product,
            "mode": "edit",
            "active_menu_item": "product_edit",
        },
    )


@staff_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        product.delete()
        messages.success(request, "Product deleted.")
        return redirect("manager:product_list")

    return render(
        request,
        "manager/product_confirm_delete.html",
        {
            "product": product,
            "active_menu_item": "product_delete",
        },
    )


@staff_required
@require_POST
def product_image_delete(request, product_id, image_id):
    product = get_object_or_404(Product, pk=product_id)
    image = get_object_or_404(ProductImage, pk=image_id, product=product)

    image.delete()
    messages.success(request, "Image deleted.")
    return redirect("manager:product_edit", pk=product.pk)


# ----------------------------
# Orders
# ----------------------------
@staff_required
def order_list(request):
    orders = Order.objects.all().order_by("-created_at")
    return render(
        request,
        "manager/order_list.html",
        {
            "orders": orders,
            "active_menu_item": "orders",
        },
    )


@staff_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(
        request,
        "manager/order_detail.html",
        {
            "order": order,
            "active_menu_item": "orders",
        },
    )
