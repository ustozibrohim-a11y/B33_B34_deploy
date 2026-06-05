from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django_filters.rest_framework.backends import DjangoFilterBackend

from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema

import src.core.models as models
import src.api.serializers as serializers


class ProductListAPIView(ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    search_fields = ["name", "id"]
    filterset_fields = ["category"]
    filter_backends = [SearchFilter, DjangoFilterBackend]


class ProductDetailAPIView(RetrieveAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductDetailSerializer


class WriteCommentAPIView(APIView):
    @extend_schema(request=serializers.WriteCommentSerializer,
                   responses={"status": bool})
    def post(self, request):
        try:
            user = request.user
            data = request.data
            product = get_object_or_404(models.Product, pk=data.get("product_id"))
            comment = data.get("comment")
            models.Comment.objects.create(user=user, product=product, comment=comment)
            return Response({"status": True})
        except Exception as e:
            return Response({"status": False, "error": str(e)})


class CommentsListAPIView(ListAPIView):
    queryset = models.Comment.objects.all()
    filterset_fields = ["product"]
    filter_backends = [DjangoFilterBackend]
    serializer_class = serializers.CommentSerializer
