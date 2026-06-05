from rest_framework.generics import ListAPIView

import src.core.models as models
import src.api.serializers as serializers


class CategoryListAPIView(ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
