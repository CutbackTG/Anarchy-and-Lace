from django.urls import path
from . import views
from . import webhooks

app_name = "payments"

urlpatterns = [
    path("create/", views.create_checkout_session, name="create"),
    path("success/", views.success, name="success"),
    path("cancel/", views.cancel, name="cancel"),
    path("webhook/", webhooks.stripe_webhook, name="stripe-webhook"),
]
