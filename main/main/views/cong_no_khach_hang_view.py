from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from main.models.cong_no_models import CongNoKhachHangModel
from main.serializers.khach_hang_ser import CongNoKhachHangSerializer


class CongNoKhachHangView(ModelViewSet):
    serializer_class = CongNoKhachHangSerializer
    queryset = CongNoKhachHangModel.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["id"]
