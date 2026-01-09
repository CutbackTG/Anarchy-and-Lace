from django.conf import settings
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")

    full_name = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=30, blank=True)

    address_line1 = models.CharField(max_length=255, blank=True)
    address_line2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=80, blank=True)
    postcode = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return f"Profile({self.user})"
