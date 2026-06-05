from src.core.models.base import *


class Cart(BaseModel):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="cart")
    total_price = models.DecimalField(max_digits=16, decimal_places=2, default=0.00)
    is_active = models.BooleanField(default=True)

    def calculate_total(self):
        items = self.items.all()
        total = 0
        for i in items:
            total += i.total_sum
        self.total_price = total
        self.save()

    def __str__(self):
        return f"{self.owner} | {self.added_at.strftime('%Y-%m-%d %H:%M')}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="cart_item")
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=16, decimal_places=2, default=0.00)
    total_sum = models.DecimalField(max_digits=16, decimal_places=2, default=0.00)

    def save(
            self,
            force_insert=False,
            force_update=False,
            using=None,
            update_fields=None,
    ):
        self.price = self.product.price
        self.total_sum = self.price * self.quantity
        super().save()

    def __str__(self):
        return f"{self.cart} | {self.product.name}"
