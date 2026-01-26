from django.conf import settings
from django.db import models

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(
        "catalog.Product",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reviews",
    )

    rating = models.PositiveSmallIntegerField(default=5)
    comment = models.TextField()

    featured = models.BooleanField(default=False)
    display_name = models.CharField(max_length=80, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def name_for_display(self):
        if self.display_name:
            return self.display_name
        full = getattr(self.user, "get_full_name", lambda: "")()
        return full or getattr(self.user, "username", "Customer")

    def __str__(self):
        return f"{self.name_for_display()} ({self.rating}/5)"
