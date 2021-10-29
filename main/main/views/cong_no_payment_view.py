from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from main.models.cong_no_models import CongNoPaymentModel
from main.serializers.cong_no_payment_ser import CongNoPaymentSerializer


class CongNoPaymentView(ModelViewSet):
    serializer_class = CongNoPaymentSerializer
    queryset = CongNoPaymentModel.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["khach_hang"]

    def get_queryset(self):
        return super().get_queryset().order_by("-date")
