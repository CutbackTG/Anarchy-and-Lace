from django import forms
from allauth.account.forms import SignupForm
from .models import Profile

class CustomerSignupForm(SignupForm):
    full_name = forms.CharField(max_length=120, label="Full name")
    phone_number = forms.CharField(max_length=30, label="Contact number", required=False)

    address_line1 = forms.CharField(max_length=255, label="Address line 1", required=False)
    address_line2 = forms.CharField(max_length=255, label="Address line 2", required=False)
    city = forms.CharField(max_length=80, label="Town / City", required=False)
    postcode = forms.CharField(max_length=20, label="Postcode", required=False)
    country = forms.CharField(max_length=60, label="Country", required=False)

    def save(self, request):
        user = super().save(request)

        Profile.objects.update_or_create(
            user=user,
            defaults={
                "full_name": self.cleaned_data["full_name"],
                "phone_number": self.cleaned_data.get("phone_number", ""),
                "address_line1": self.cleaned_data.get("address_line1", ""),
                "address_line2": self.cleaned_data.get("address_line2", ""),
                "city": self.cleaned_data.get("city", ""),
                "postcode": self.cleaned_data.get("postcode", ""),
                "country": self.cleaned_data.get("country", ""),
            },
        )
        return user
