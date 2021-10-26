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

    def get_queryset(self):
        start = self.request.query_params.get('start')
        end = self.request.query_params.get('end')
        if start and end:
            queryset = XuatNhapTonModel.objects.filter(updated_on__range=[start, end]).filter(so_luong_nhap__gt=0)
        else:
            queryset = super().get_queryset().filter(so_luong_nhap__gt=0)
        return queryset.order_by("-id")
