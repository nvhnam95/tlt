from rest_framework.viewsets import ModelViewSet

from main.models.xuat_kho_model import XuatKhoModel
from main.serializers.xuat_kho_ser import XuatKhoSerializer


class XuatKhoView(ModelViewSet):
    serializer_class = XuatKhoSerializer
    queryset = XuatKhoModel.objects.all()
