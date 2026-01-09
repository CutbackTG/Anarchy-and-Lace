from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from core.models import Profile

User = get_user_model()


class ProfileViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
        username="customer1",
        email="customer1@example.com",
        password="V3ry$trongPassphrase!2026",
        )

        Profile.objects.update_or_create(
            user=self.user,
            defaults={
                "full_name": "Tyler Worth",
                "phone_number": "+447700900123",
                "address_line1": "10 Gold Street",
                "address_line2": "",
                "city": "London",
                "postcode": "SW1A 1AA",
                "country": "United Kingdom",
            },
        )

    def test_profile_page_requires_login(self):
        url = reverse("core:profile")
        res = self.client.get(url)
        self.assertIn(res.status_code, (302, 303))  # redirect to login

    def test_profile_page_shows_saved_details(self):
        self.client.login(email="customer1@example.com", password="V3ry$trongPassphrase!2026")

        url = reverse("core:profile")
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "Tyler Worth")
        self.assertContains(res, "+447700900123")
        self.assertContains(res, "10 Gold Street")
        self.assertContains(res, "London")
        self.assertContains(res, "SW1A 1AA")
        self.assertContains(res, "United Kingdom")
