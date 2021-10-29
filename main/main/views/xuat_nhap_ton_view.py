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

    def list(self, request, *args, **kwargs):
        results = super().list(request, *args, **kwargs)
        grouped_dict = {}
        grouped_arr = []
        for item in results.data:
            pn_10 = item["pn_13"][:10]
            if pn_10 in grouped_dict:
                grouped_dict[pn_10]["so_luong_nhap"] += item["so_luong_nhap"]
                grouped_dict[pn_10]["so_luong_xuat"] += item["so_luong_xuat"]
                grouped_dict[pn_10]["ton_cuoi"] += item["ton_cuoi"]
                grouped_dict[pn_10]["total_po"] += item["total_po"]
                grouped_dict[pn_10]["bor"] += item["bor"]
                grouped_dict[pn_10]["bor_price"] += item["bor_price"]
                grouped_dict[pn_10]["gia_si"] += item["gia_si"]
                grouped_dict[pn_10]["gia_le"] += item["gia_le"]
            else:
                grouped_dict[pn_10] = item
        for pn_10 in grouped_dict:
            d = grouped_dict[pn_10]

            d["pn_10"] = pn_10
            grouped_arr.append(d)

        results.data = grouped_arr
        return results
