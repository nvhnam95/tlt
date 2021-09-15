from rest_framework.viewsets import ModelViewSet

from main.models.xuat_nhap_ton_model import XuatNhapTonModel
from main.serializers.xuat_nhap_ton_ser import XuatNhapTonSerializer


class XuatNhapTonView(ModelViewSet):
    serializer_class = XuatNhapTonSerializer
    queryset = XuatNhapTonModel.objects.all()
