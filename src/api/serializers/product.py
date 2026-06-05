from src.api.serializers.base import *


class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductImage
        fields = ["id", "image"]


class ProductDetailSerializer(BaseSerializer):
    class Meta:
        model = models.Product
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["description"] = instance.description.html
        data["category"] = CategoryRelationSerializer(instance.category).data
        data["images"] = ProductImagesSerializer(instance.images.all(), many=True).data
        return data


class WriteCommentSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(default=0)
    comment = serializers.CharField(max_length=500)


class CommentSerializer(BaseSerializer):
    class Meta:
        model = models.Comment
        fields = ["user", "comment"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["user"] = UserRelationSerializer(instance.user).data
        return data
