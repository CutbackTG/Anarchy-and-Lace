from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render

from catalog.models import Product
from .decorators import staff_required
from .forms import ProductForm


class StaffOnlyAuthenticationForm(AuthenticationForm):
    """Normal username/password form, but only allow staff to authenticate."""
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
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("manager:product_list")
    else:
        form = ProductForm()

    return render(request, "manager/product_form.html", {"form": form, "mode": "create"})


@staff_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("manager:product_list")
    else:
        form = ProductForm(instance=product)

    return render(request, "manager/product_form.html", {"form": form, "product": product, "mode": "edit"})


@staff_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        product.delete()
        return redirect("manager:product_list")

    return render(request, "manager/product_confirm_delete.html", {"product": product})
