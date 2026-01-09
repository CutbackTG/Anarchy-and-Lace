from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "image",
            "name",
            "description",
            "price",
            "sku",
            "stock_qty",
            "size",
            "fit_notes",
            "fabric_origin",
            "is_active",
            "collections",
        ]
