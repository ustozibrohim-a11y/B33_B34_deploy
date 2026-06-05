from rest_framework import serializers

import src.core.models as models


class CategoryRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ("id", "name")


class UserRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ("id", "username")


class BaseSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["added_at"] = instance.added_at.strftime("%Y-%m-%d %H:%M")
        data["updated_at"] = instance.updated_at.strftime("%Y-%m-%d %H:%M")
        return data


class ProductSerializer(BaseSerializer):
    class Meta:
        model = models.Product
        fields = ("id", "name", "category", "image", "price", "stock")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["category"] = CategoryRelationSerializer(instance.category).data
        return data
