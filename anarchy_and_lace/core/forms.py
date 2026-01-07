import re

from django import forms
from django.core.exceptions import ValidationError

from allauth.account.forms import SignupForm

from core.models import Profile


class CustomerSignupForm(SignupForm):
    """
    Extended signup form used by django-allauth.

    Adds customer profile fields and validates them before
    account creation. Profile is created on successful signup.
    """

    full_name = forms.CharField(
        max_length=120,
        required=True,
        label="Full name"
    )

    phone_number = forms.CharField(
        max_length=30,
        required=True,
        label="Contact number"
    )

    address_line1 = forms.CharField(
        max_length=255,
        required=True,
        label="Address line 1"
    )

    address_line2 = forms.CharField(
        max_length=255,
        required=False,
        label="Address line 2"
    )

    city = forms.CharField(
        max_length=80,
        required=True,
        label="Town / City"
    )

    postcode = forms.CharField(
        max_length=20,
        required=True,
        label="Postcode"
    )

    country = forms.CharField(
        max_length=60,
        required=True,
        label="Country"
    )

    # ---------- FIELD VALIDATION ----------

    def clean_full_name(self):
        name = (self.cleaned_data.get("full_name") or "").strip()
        if len(name) < 2:
            raise ValidationError("Please enter your full name.")
        if " " not in name:
            raise ValidationError("Please include both first and last name.")
        return name

    def clean_phone_number(self):
        phone = (self.cleaned_data.get("phone_number") or "").strip()
        if not re.fullmatch(r"[0-9+\-\s()]{7,30}", phone):
            raise ValidationError("Please enter a valid contact number.")
        return phone

    def clean_postcode(self):
        postcode = (self.cleaned_data.get("postcode") or "").strip()
        if len(postcode) < 3:
            raise ValidationError("Please enter a valid postcode.")
        return postcode.upper()

    # ---------- SAVE ----------

    def save(self, request):
        """
        Called by allauth after the form is valid.
        Creates the user, then the related Profile.
        """
        user = super().save(request)

        Profile.objects.update_or_create(
            user=user,
            defaults={
                "full_name": self.cleaned_data["full_name"],
                "phone_number": self.cleaned_data["phone_number"],
                "address_line1": self.cleaned_data["address_line1"],
                "address_line2": self.cleaned_data.get("address_line2", ""),
                "city": self.cleaned_data["city"],
                "postcode": self.cleaned_data["postcode"],
                "country": self.cleaned_data["country"],
            },
        )

        return user
