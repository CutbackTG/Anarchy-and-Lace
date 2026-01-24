from cloudinary.models import CloudinaryField

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)
    image = CloudinaryField("image", folder="products")
