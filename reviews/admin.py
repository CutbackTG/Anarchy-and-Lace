from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "featured", "created_at")
    list_filter = ("featured", "created_at")
    search_fields = ("comment",)
