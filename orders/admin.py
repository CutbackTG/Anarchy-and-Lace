from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ("product_name", "sku", "unit_price", "quantity", "line_total")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_number", "status", "email", "total", "currency", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("order_number", "email", "stripe_checkout_session_id", "stripe_payment_intent_id")
    readonly_fields = ("order_number", "created_at", "updated_at", "stripe_checkout_session_id", "stripe_payment_intent_id")
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product_name", "quantity", "unit_price", "line_total")
    search_fields = ("product_name", "sku", "order__order_number")
