from django.contrib import admin
from .models import Collection, Product, ProductImage


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "sku", "price", "stock_qty", "is_active", "created_at")
    list_filter = ("is_active", "collections")
    search_fields = ("name", "sku", "description", "fabric_origin")
    list_select_related = ()
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ProductImageInline]
    ordering = ("-created_at",)


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("product", "is_primary", "sort_order")
    list_filter = ("is_primary",)
    search_fields = ("product__name", "product__sku", "alt_text")
    ordering = ("product", "sort_order", "id")
