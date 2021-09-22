from rest_framework.viewsets import ModelViewSet

from main.models.xuat_kho_model import XuatKhoModel
from main.serializers.xuat_kho_ser import XuatKhoSerializer
from main.utils.xuat_nhap_ton_service import refresh_xnt


class XuatKhoView(ModelViewSet):
    serializer_class = XuatKhoSerializer
    queryset = XuatKhoModel.objects.all()

    def destroy(self, request, *args, **kwargs):
        xuat_kho_obj = self.get_object()
        res = super().destroy(request, *args, **kwargs)
        refresh_xnt(xuat_kho_obj.pn_13)
        return res
