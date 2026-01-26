from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "comment", "display_name"]
        widgets = {
            "rating": forms.NumberInput(attrs={"min": 1, "max": 5}),
            "comment": forms.Textarea(attrs={"rows": 4}),
            "display_name": forms.TextInput(attrs={"placeholder": "Name shown publicly (optional)"}),
        }
        
widgets = {
    "comment": forms.Textarea(attrs={"rows": 4, "maxlength": 300}),
}
