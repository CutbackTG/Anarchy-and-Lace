from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ("product", "product_name", "sku", "unit_price", "quantity", "line_total")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_number", "user", "email", "status", "created_at", "total", "currency")
    list_filter = ("status", "created_at", "currency")
    search_fields = ("order_number", "email", "user__email", "stripe_checkout_session_id", "stripe_payment_intent_id")
    ordering = ("-created_at",)

    # This lets you change status straight from the list page without opening the order
    list_editable = ("status",)

    readonly_fields = ("order_number", "created_at", "updated_at")

    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product_name", "quantity", "unit_price", "line_total")
    search_fields = ("order__order_number", "product_name", "sku")
    ordering = ("-id",)
