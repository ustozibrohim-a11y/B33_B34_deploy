from src.core.models.base import *


class Category(BaseModel):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null=True, related_name="products")
    image = models.ImageField(upload_to="products/")
    description = QuillField()
    price = models.DecimalField(max_digits=16, decimal_places=2, default=0.00)  # 15.05
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="product_images/")


class Stock(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name="stocks")
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=16, decimal_places=2, default=0.00)
    total_sum = models.DecimalField(max_digits=16, decimal_places=2, default=0.00)

    def save(
            self,
            force_insert=False,
            force_update=False,
            using=None,
            update_fields=None,
    ):
        self.total_sum = self.price * self.quantity  # 20 = 5 * 4
        super().save()

    def __str__(self):
        return f"{self.product.name} | {self.added_at.strftime('%Y-%m-%d %H:%M')}"  # 20250606T12231245 -> 2025-06-06 12:23


class Comment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="comments")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ["-id"]
