from django import forms
from catalog.models import Product


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
            "care_instructions",
            "fabric_origin",
            "is_active",
            "collections",
        ]

        widgets = {
            "description": forms.Textarea(attrs={"rows": 4}),
        }

