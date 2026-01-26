from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path("add/<str:order_number>/<int:product_id>/", views.add_review_from_order, name="add_from_order"),
]
