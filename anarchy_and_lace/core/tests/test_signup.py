from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from core.models import Profile

User = get_user_model()


class SignupValidationTests(TestCase):
    """
    STEP 1 (RED): Write tests first.

    Requirements:
    - Users can sign up
    - Signup requires: full_name, email, phone_number, address_line1, city, postcode, country
    - On success: redirect (302/303) and create Profile with saved fields
    """

    def setUp(self):
        self.url = reverse("account_signup")

    def _valid_payload(self, **overrides):
        payload = {
    "email": "tyler1@example.com",
    "password1": "V3ry$trongPassphrase!2026",
    "password2": "V3ry$trongPassphrase!2026",

    "full_name": "Tyler Worth",
    "phone_number": "+447700900123",
    "address_line1": "10 Gold Street",
    "address_line2": "",
    "city": "London",
    "postcode": "SW1A 1AA",
    "country": "United Kingdom",
    }
        payload.update(overrides)
        return payload

    # ---------- VALIDATION (must stay on page = 200) ----------

    def test_signup_rejects_missing_full_name(self):
        res = self.client.post(self.url, data=self._valid_payload(full_name=""))
        self.assertEqual(res.status_code, 200)

    def test_signup_rejects_missing_phone_number(self):
        res = self.client.post(self.url, data=self._valid_payload(phone_number=""))
        self.assertEqual(res.status_code, 200)

    def test_signup_rejects_missing_address_fields(self):
        res = self.client.post(
            self.url,
            data=self._valid_payload(address_line1="", city="", postcode="", country="")
        )
        self.assertEqual(res.status_code, 200)

    # ---------- HAPPY PATH (should redirect + create profile) ----------

    def test_success_signup_creates_profile_and_saves_fields(self):
        res = self.client.post(self.url, data=self._valid_payload())

        # On success, allauth should redirect away from signup page
        self.assertIn(res.status_code, (302, 303))

        # Find the created user (prefer email because username may be optional)
        user = User.objects.get(email="tyler1@example.com")

        # Profile must exist and contain saved extended fields
        profile = Profile.objects.get(user=user)
        self.assertEqual(profile.full_name, "Tyler Worth")
        self.assertEqual(profile.phone_number, "+447700900123")
        self.assertEqual(profile.address_line1, "10 Gold Street")
        self.assertEqual(profile.city, "London")
        self.assertEqual(profile.postcode, "SW1A 1AA")
        self.assertEqual(profile.country, "United Kingdom")

        def test_signup_rejects_short_full_name(self):
            res = self.client.post(
            self.url,
            data=self._valid_payload(full_name="Ty")
        )
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "Full name must be at least 3 characters")

    def test_signup_rejects_short_phone_number(self):
        res = self.client.post(
            self.url,
            data=self._valid_payload(phone_number="123")
        )
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "Enter a valid phone number")

    def test_signup_rejects_short_password(self):
        res = self.client.post(
            self.url,
            data=self._valid_payload(
                password1="abc123",
                password2="abc123"
            )
        )
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "This password is too short")

    def test_signup_rejects_short_address(self):
        res = self.client.post(
            self.url,
            data=self._valid_payload(address_line1="1")
        )
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "Address must be at least 5 characters")

