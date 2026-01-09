from allauth.account.forms import SignupForm
from django import forms
from django.core.exceptions import ValidationError

from core.models import Profile


class CustomerSignupForm(SignupForm):
    full_name = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=20)
    address_line1 = forms.CharField(max_length=255)
    address_line2 = forms.CharField(required=False)
    city = forms.CharField(max_length=100)
    postcode = forms.CharField(max_length=20)
    country = forms.CharField(max_length=100)

    def clean_full_name(self):
        full_name = self.cleaned_data.get("full_name", "").strip()
        if len(full_name) < 3:
            raise ValidationError("Full name must be at least 3 characters")
        return full_name

    def clean_phone_number(self):
        phone = self.cleaned_data.get("phone_number", "").strip()
        if len(phone) < 7:
            raise ValidationError("Enter a valid phone number")
        return phone

    def clean_address_line1(self):
        addr = self.cleaned_data.get("address_line1", "").strip()
        if len(addr) < 5:
            raise ValidationError("Address must be at least 5 characters")
        return addr

    def save(self, request):
        user = super().save(request)

        Profile.objects.create(
            user=user,
            full_name=self.cleaned_data["full_name"],
            phone_number=self.cleaned_data["phone_number"],
            address_line1=self.cleaned_data["address_line1"],
            address_line2=self.cleaned_data.get("address_line2", ""),
            city=self.cleaned_data["city"],
            postcode=self.cleaned_data["postcode"],
            country=self.cleaned_data["country"],
        )

        return user
