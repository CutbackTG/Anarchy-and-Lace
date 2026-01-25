from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "text"]
        widgets = {
            "text": forms.Textarea(attrs={
                "rows": 5,
                "maxlength": 300,
                "placeholder": "Keep it short and sharp…",
                "style": "width:100%; border-radius:14px; padding:12px; border:1px solid var(--panel-border);",
            }),
        }
