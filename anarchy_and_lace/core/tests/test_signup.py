from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from core.models import Profile

User = get_user_model()


class SignupValidationTests(TestCase):
    def setUp(self):
        self.url = reverse("account_signup")

    def _valid_payload(self, **overrides):
        payload = {
            "username": "tyler1",
            "email": "tyler1@example.com",
            "password1": "StrongPass123!StrongPass123!",
            "password2": "StrongPass123!StrongPass123!",
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

    def test_signup_rejects_missing_full_name(self):
        res = self.client.post(self.url, data=self._valid_payload(full_name=""))
        self.assertEqual(res.status_code, 200)  # stays on page = form invalid

    def test_signup_rejects_missing_phone_number(self):
        res = self.client.post(self.url, data=self._valid_payload(phone_number=""))
        self.assertEqual(res.status_code, 200)

    def test_signup_rejects_missing_address_fields(self):
        res = self.client.post(
            self.url,
            data=self._valid_payload(address_line1="", city="", postcode="", country="")
        )
        self.assertEqual(res.status_code, 200)

    def test_success_signup_creates_profile_and_saves_fields(self):
        res = self.client.post(self.url, data=self._valid_payload())
        self.assertIn(res.status_code, (302, 303))  # successful signup redirects

        user = User.objects.get(username="tyler1")
        profile = Profile.objects.get(user=user)

        self.assertEqual(profile.full_name, "Tyler Worth")
        self.assertEqual(profile.phone_number, "+447700900123")
        self.assertEqual(profile.address_line1, "10 Gold Street")
        self.assertEqual(profile.city, "London")
        self.assertEqual(profile.postcode, "SW1A 1AA")
        self.assertEqual(profile.country, "United Kingdom")
