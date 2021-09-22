from rest_framework.viewsets import ModelViewSet

from main.models.xuat_nhap_ton_model import XuatNhapTonModel
from main.serializers.xuat_nhap_ton_ser import XuatNhapTonSerializer
from main.utils.xuat_nhap_ton_service import refresh_xnt


class XuatNhapTonView(ModelViewSet):
    serializer_class = XuatNhapTonSerializer
    queryset = XuatNhapTonModel.objects.all()

    def destroy(self, request, *args, **kwargs):
        xnt_obj = self.get_object()
        res = super().destroy(request, *args, **kwargs)
        refresh_xnt(xnt_obj.pn_13)
        return res
