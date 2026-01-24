from django.urls import path
from . import views

app_name = "manager"

urlpatterns = [
    path("login/", views.ManagerLoginView.as_view(), name="login"),
    path("", views.dashboard, name="dashboard"),
    path("products/", views.product_list, name="product_list"),
    path("products/new/", views.product_create, name="product_create"),
    path("products/<int:pk>/edit/", views.product_edit, name="product_edit"),
    path("products/<int:pk>/delete/", views.product_delete, name="product_delete"),
    path(
        "products/<int:product_id>/images/<int:image_id>/delete/",
        views.product_image_delete,
        name="product_image_delete",
    ),
]
