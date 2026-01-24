from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["rating", "text"]
        widgets = {
            "rating": forms.RadioSelect(choices=[(i, "★" * i) for i in range(1, 6)]),
            "text": forms.Textarea(attrs={"rows": 3, "maxlength": 300, "placeholder": "Keep it short and sharp…"}),
        }

    def clean_text(self):
        text = (self.cleaned_data.get("text") or "").strip()
        return text
