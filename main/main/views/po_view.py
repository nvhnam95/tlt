from django.http import HttpResponse
from rest_framework.decorators import action
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

    @action(['post'], False, 'import-excel')
    def export_cong_no(self, request):
        data = request.data["data"]
        headers = data[0]
        if len(headers) != 20:
            return HttpResponse("Cannot import because not enough 20 columns")
        po_data = data[1:]
        for po in po_data:
            if len(po) < 1:
                continue
            validated_data = {
                "po_no":            po[0] or "",
                "pn_13":            po[1] or "",
                "pn_10":            po[2] or "",
                "bosch_no":         po[3] or "",
                "z_exel_no":         po[4] or "",
                "stamping":         po[5] or "",
                "country":          po[6] or "",
                "english_des":      po[7] or "",
                "import_des":       po[8] or "",
                "app_des":          po[9] or "",
                "tax":              po[10] or "",
                "quantity":         po[11] or 0,
                "dap_price":        po[12] or 0,
                "extension_price":  po[13] or 0,
                "gia_von":          po[14] or 0,
                "gia_si":           po[15] or 0,
                "gia_le":           po[16] or 0,
                "lead_time":        po[17] if len(po) > 17 and po[17] else "",
                "customer":         po[18] if len(po) > 18 and po[18] else "",
                "remarks":          po[19] if len(po) > 19 and po[19] else "",
            }
            POSerializer().create(validated_data)
        return HttpResponse("Done")
