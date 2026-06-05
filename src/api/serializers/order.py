from src.api.serializers.base import *


class BillingDetailSerializer(BaseSerializer):
    class Meta:
        model = models.Billing
        fields = "__all__"
