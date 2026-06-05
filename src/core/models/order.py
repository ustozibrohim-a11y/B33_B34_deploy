from src.core.models.base import *


class Billing(BaseModel):
    f_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    ex_phone = models.CharField(max_length=20, null=True, blank=True)
    payment_type = models.CharField(max_length=50, choices=[('card', 'Karta'), ('cash', "Naqt")])

    def __str__(self):
        return f"{self.f_name} | {self.added_at.strftime('%Y-%m-%d %H:%M')}"


class Order(BaseModel):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="order")
    billing = models.ForeignKey(Billing, on_delete=models.SET_NULL, null=True, related_name="order")
    total_price = models.DecimalField(max_digits=16, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.owner} | {self.added_at.strftime('%Y-%m-%d %H:%M')}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="order_item")
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=16, decimal_places=2, default=0.00)
    total_sum = models.DecimalField(max_digits=16, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.order} | {self.product.name}"
