from django.contrib import admin
from .models import Product, Collection, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "sku", "price", "stock_qty", "is_active")
    list_filter = ("is_active", "condition_grade", "collections")
    search_fields = ("name", "sku", "fabric_origin")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ProductImageInline]
