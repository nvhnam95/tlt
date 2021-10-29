from rest_framework.viewsets import ModelViewSet

from main.models.po_model import POModel
from main.serializers.po_ser import POSerializer
from django_filters.rest_framework import DjangoFilterBackend

from main.utils.xuat_nhap_ton_service import refresh_xnt


class POView(ModelViewSet):
    serializer_class = POSerializer
    queryset = POModel.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['pn_13']

    def destroy(self, request, *args, **kwargs):
        po_obj = self.get_object()
        res = super().destroy(request, *args, **kwargs)
        refresh_xnt(po_obj.pn_13)
        return res

    def get_queryset(self):
        start = self.request.query_params.get('start')
        end = self.request.query_params.get('end')
        if start and end:
            queryset = POModel.objects.filter(updated_on__range=[start, end])
        else:
            queryset = super().get_queryset()
        return queryset.order_by("-id")
