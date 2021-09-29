from main.models.nhap_kho_model import NhapKhoModel
from main.models.xuat_kho_model import XuatKhoModel
from main.models.xuat_nhap_ton_model import XuatNhapTonModel


def calculate_gia_goc_xuat_kho(pn_13):
    recent_xuat_kho = XuatKhoModel.objects.filter(pn_13=pn_13).last()

    if recent_xuat_kho:
        # Find any nhap_kho after last xuat_kho
        recent_nhap_kho_objecs = NhapKhoModel.objects.filter(pn_13=pn_13, input_date__gt=recent_xuat_kho.input_date)
        xuat_nhap_ton = XuatNhapTonModel.objects.filter(pn_13=pn_13).first()
        ton_cuoi = xuat_nhap_ton.ton_cuoi

        if recent_nhap_kho_objecs:
            pass
        # Weighted average
        total_price = recent_xuat_kho.gia_goc * ton_cuoi + sum([n.quantity * n.gia_goc for n in recent_nhap_kho_objecs])
        total_amount = ton_cuoi + sum([n.quantity for n in recent_nhap_kho_objecs])
        weighted_average_price = total_price / total_amount
    else:
        recent_nhap_kho_objecs = NhapKhoModel.objects.filter(pn_13=pn_13)
        if not recent_nhap_kho_objecs:
            return 0
        # Weighted average
        total_price = sum([n.quantity * n.gia_goc for n in recent_nhap_kho_objecs])
        total_amount = sum([n.quantity for n in recent_nhap_kho_objecs])
        weighted_average_price = total_price / total_amount
    return weighted_average_price
