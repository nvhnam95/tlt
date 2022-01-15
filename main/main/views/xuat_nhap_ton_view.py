from rest_framework.viewsets import ModelViewSet

from main.models.nhap_kho_model import NhapKhoModel
from main.models.po_model import POModel
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
            queryset = super().get_queryset()
        return queryset.order_by("-id")

    def list(self, request, *args, **kwargs):
        results = super().list(request, *args, **kwargs)
        grouped_dict = {}
        grouped_arr = []
        for item in results.data:
            pn_13 = item["pn_13"]
            pn_10 = pn_13[:10]
            total_po_price = sum([po.extension_price for po in POModel.objects.filter(pn_10=pn_10)])
            total_nhap_kho_price = sum([nk.extension_price for nk in NhapKhoModel.objects.filter(pn_10=pn_10)])
            if pn_10 in grouped_dict:
                grouped_dict[pn_10]["so_luong_nhap"] += item["so_luong_nhap"]
                grouped_dict[pn_10]["so_luong_xuat"] += item["so_luong_xuat"]
                grouped_dict[pn_10]["ton_cuoi"] += item["ton_cuoi"]
                grouped_dict[pn_10]["total_po"] += item["total_po"]
                grouped_dict[pn_10]["bor"] += item["bor"]

                grouped_dict[pn_10]["gia_si"] = max(item["gia_si"], grouped_dict[pn_10]["gia_si"])
                grouped_dict[pn_10]["gia_le"] = max(item["gia_le"], grouped_dict[pn_10]["gia_le"])
            else:
                grouped_dict[pn_10] = item
            bor_price = total_po_price - total_nhap_kho_price
            grouped_dict[pn_10]["bor_price"] = bor_price

        for pn_10 in grouped_dict:
            d = grouped_dict[pn_10]

            d["pn_10"] = pn_10
            grouped_arr.append(d)

        results.data = grouped_arr
        return results
