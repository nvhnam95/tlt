from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ModelViewSet

from main.models.xuat_kho_model import XuatKhoModel
from main.serializers.xuat_kho_ser import XuatKhoSerializer
from main.utils.pricing_service import calculate_gia_goc_xuat_kho
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
        xuat_kho_id = request.query_params.get('id')
        input_date = request.query_params.get('input_date')
        if not pn_13:
            return Response("pn_13 is required", status=HTTP_400_BAD_REQUEST)

        gia_goc = calculate_gia_goc_xuat_kho(pn_13, xuat_kho_id, input_date)

        return Response(gia_goc)

    def get_queryset(self):
        start = self.request.query_params.get('start')
        end = self.request.query_params.get('end')
        if start and end:
            queryset = XuatKhoModel.objects.filter(input_date__range=[start, end])
        else:
            queryset = super().get_queryset()
        return queryset.order_by("-input_date")
