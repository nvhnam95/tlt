from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from main.models.cong_no_models import CongNoModel
from main.serializers.cong_no_ser import CongNoSerializer


class CongNoView(ModelViewSet):
    serializer_class = CongNoSerializer
    queryset = CongNoModel.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["khach_hang"]
