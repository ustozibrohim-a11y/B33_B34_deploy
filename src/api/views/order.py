from rest_framework.views import APIView
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema

import src.service as service
import src.core.models as models
import src.api.serializers as serializers


class OrderAPIView(APIView):
    @extend_schema(
        request=serializers.BillingDetailSerializer,
        responses=serializers.BillingDetailSerializer
    )
    def post(self, request):
        user = request.user
        data = request.data
        serializer = serializers.BillingDetailSerializer(data=data)
        cart = models.Cart.objects.filter(owner=user, is_active=True).first()  # [item] -> item
        items = models.CartItem.objects.filter(cart=cart)
        if serializer.is_valid():
            billing = serializer.save()
            service.OrderAddService.add_order(user, cart, items, billing)
            return Response(serializer.data)
        return Response(serializer.errors)
