from src.core.models.base import *


class Wishlist(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wishlist")
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="wishlist")

    def __str__(self):
        return f"{self.user.id} | {self.product.id} | {self.added_at.strftime('%Y-%m-%d %H:%M')}"
