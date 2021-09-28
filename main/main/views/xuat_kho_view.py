from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ModelViewSet

from main.models.nhap_kho_model import NhapKhoModel
from main.models.xuat_kho_model import XuatKhoModel
from main.models.xuat_nhap_ton_model import XuatNhapTonModel
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

    @action(['get'], False, 'calculate-gia-goc')
    def calculate_gia_goc(self, request):
        pn_13 = request.query_params.get('pn_13')
        if not pn_13:
            return Response("pn_13 is required", status=HTTP_400_BAD_REQUEST)

        recent_xuat_kho = XuatKhoModel.objects.filter(pn_13=pn_13).last()

        if recent_xuat_kho:
            # Find any nhap_kho after last xuat_kho
            recent_nhap_kho_objecs = NhapKhoModel.objects.filter(pn_13=pn_13, created_at__gt=recent_xuat_kho.created_at)
            xuat_nhap_ton = XuatNhapTonModel.objects.filter(pn_13=pn_13).first()
            ton_cuoi = xuat_nhap_ton.ton_cuoi

            # Weighted average
            total_price = recent_xuat_kho.gia_goc * ton_cuoi + sum([n.quantity * n.gia_goc for n in recent_nhap_kho_objecs])
            total_amount = ton_cuoi + sum([n.quantity for n in recent_nhap_kho_objecs])
            weighted_average_price = total_price / total_amount
        else:
            recent_nhap_kho_objecs = NhapKhoModel.objects.filter(pn_13=pn_13)
            if not recent_nhap_kho_objecs:
                return Response('')
            # Weighted average
            total_price = sum([n.quantity * n.gia_goc for n in recent_nhap_kho_objecs])
            total_amount = sum([n.quantity for n in recent_nhap_kho_objecs])
            weighted_average_price = total_price / total_amount
        return Response(round(weighted_average_price, 2))

