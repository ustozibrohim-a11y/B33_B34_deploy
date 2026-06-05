from src.api.serializers.base import *


class AddToCartSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(default=0)


class FixQuantitySerializer(serializers.Serializer):
    item_id = serializers.IntegerField(default=0)
    type = serializers.ChoiceField(choices=['add', 'remove'])


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CartItem
        exclude = ["cart"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["product"] = ProductSerializer(instance.product).data
        return data

class CartSerializer(BaseSerializer):
    class Meta:
        model = models.Cart
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["owner"] = UserRelationSerializer(instance.owner).data
        data["items"] = CartItemSerializer(instance.items.all(), many=True).data
        return data
