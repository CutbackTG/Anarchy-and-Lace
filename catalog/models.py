from django.db import models
from django.utils.text import slugify


class Collection(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=90, unique=True, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Product(models.Model):
    # Primary image (simple single image field)
    image = models.ImageField(upload_to="products/", blank=True, null=True)

    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True, blank=True)

    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    sku = models.CharField(max_length=40, unique=True)
    stock_qty = models.PositiveIntegerField(default=0)

    size = models.CharField(max_length=20, blank=True)  # e.g. S/M/L or "One size"
    fit_notes = models.CharField(max_length=140, blank=True)
    care_instructions = models.CharField(max_length=140, blank=True)

    fabric_origin = models.CharField(max_length=140, blank=True)  # e.g. "Taisho-era kimono silk"

    is_active = models.BooleanField(default=True)
    collections = models.ManyToManyField(Collection, blank=True, related_name="products")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.name} ({self.sku})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class ProductImage(models.Model):
    """
    Optional: additional images (gallery).
    Keep this even if you use the main Product.image,
    it lets you add multiple images later.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="products/")
    alt_text = models.CharField(max_length=120, blank=True)
    is_primary = models.BooleanField(default=False)
    sort_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["sort_order", "id"]

    def __str__(self) -> str:
        return f"Image for {self.product.sku}"

    def save(self, *args, **kwargs):
        # Ensure only one primary image per product
        if self.is_primary:
            ProductImage.objects.filter(product=self.product, is_primary=True).exclude(pk=self.pk).update(
                is_primary=False
            )
        super().save(*args, **kwargs)
