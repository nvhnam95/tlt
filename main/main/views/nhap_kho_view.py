from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from main.models.nhap_kho_model import NhapKhoModel
from main.serializers.nhap_kho_ser import NhapKhoSerializer
from main.utils.xuat_nhap_ton_service import refresh_xnt


class NhapKhoView(ModelViewSet):
    serializer_class = NhapKhoSerializer
    queryset = NhapKhoModel.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['pn_13']

    def destroy(self, request, *args, **kwargs):
        nhap_kho_obj = self.get_object()
        res = super().destroy(request, *args, **kwargs)
        refresh_xnt(nhap_kho_obj.pn_13)
        return res

    def get_queryset(self):
        start = self.request.query_params.get('start')
        end = self.request.query_params.get('end')
        if start and end:
            queryset = NhapKhoModel.objects.filter(input_date__range=[start, end])
        else:
            queryset = super().get_queryset()
        return queryset
