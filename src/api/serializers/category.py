from src.api.serializers.base import *


class CategorySerializer(BaseSerializer):
    class Meta:
        model = models.Category
        fields = "__all__"
