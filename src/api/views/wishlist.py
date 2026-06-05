from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema

import src.core.models as models
import src.api.serializers as serializers


class AddRemoveWishlistView(APIView):
    @extend_schema(request=serializers.WishlistAddRemoveSerializer,
                   responses={"status": bool})
    def post(self, request):
        user = request.user
        product_id = request.data.get("product_id")  # 1, 2, 45
        product = get_object_or_404(models.Product, pk=product_id)
        item, created = models.Wishlist.objects.get_or_create(user=user, product=product)
        if not created:
            item.delete()
        return Response({"success": True})


class WishlistView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        object_list = models.Wishlist.objects.filter(user=user).order_by("-added_at")
        serializer = serializers.WishlistSerializer(object_list, many=True)
        return Response(serializer.data)
