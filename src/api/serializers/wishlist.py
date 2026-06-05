from src.api.serializers.base import *


class WishlistAddRemoveSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(default=0)


class WishlistSerializer(BaseSerializer):
    class Meta:
        model = models.Wishlist
        exclude = ["user"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["product"] = ProductSerializer(instance.product).data
        return data