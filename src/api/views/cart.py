from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema

import src.core.models as models
import src.api.serializers as serializers


class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        cart, _ = models.Cart.objects.get_or_create(owner=user, is_active=True)
        serializer = serializers.CartSerializer(cart)
        return Response(serializer.data)


class AddToCartView(APIView):
    @extend_schema(
        request=serializers.AddToCartSerializer,
        responses={"status": bool}
    )
    def post(self, request):
        user = request.user
        product_id = request.data.get("product_id")
        product = get_object_or_404(models.Product, pk=product_id)
        cart, _ = models.Cart.objects.get_or_create(owner=user, is_active=True)
        item, created = models.CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            item.quantity += 1
            item.save()
        cart.calculate_total()
        return Response({"status": True})


class FixQuantityView(APIView):
    @extend_schema(
        request=serializers.FixQuantitySerializer,
        responses={"status": bool}
    )
    def post(self, request):
        item_id = request.data.get('item_id')
        action = request.data.get('type')
        item = get_object_or_404(models.CartItem, pk=item_id)
        cart = get_object_or_404(models.Cart, pk=item.cart.pk)
        if action == "add":
            item.quantity += 1
            item.save()
        elif action == "remove":
            item.quantity -= 1
            if item.quantity == 0:
                item.delete()
            else:
                item.save()
        else:
            return Response({"status": False, "msg": "UnKnown type"})
        cart.calculate_total()
        return Response({"status": True})
