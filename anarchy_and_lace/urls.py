from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),

    # Authentication (django-allauth)
    path("accounts/", include("allauth.urls")),

    # Manager / staff dashboard
    path("manager/", include(("manager.urls", "manager"), namespace="manager")),

    # Shop / catalogue
    path("shop/", include(("catalog.urls", "catalog"), namespace="catalog")),

    # Core (profiles etc.)
    path("", include(("core.urls", "core"), namespace="core")),

    # Home / landing pages
    path("", include(("home.urls", "home"), namespace="home")),
    
    # Cart
    path("cart/", include(("cart.urls", "cart"), namespace="cart")),

    # Payments
    path("payments/", include(("payments.urls", "payments"), namespace="payments")),

    # Orders
    path("orders/", include("orders.urls")),

    # Reviews
    path("reviews/", include("reviews.urls", namespace="reviews")),

]

# Media files (product images etc.) – dev only
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
