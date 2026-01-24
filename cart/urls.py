from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("", views.cart_view, name="cart"),
    path("add/<int:product_id>/", views.cart_add, name="add"),
    path("remove/<int:product_id>/", views.cart_remove, name="remove"),
    path("set/<int:product_id>/", views.cart_set_qty, name="set_qty"),
    path("clear/", views.cart_clear, name="clear"),
]
