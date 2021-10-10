from datetime import datetime

from main.models.nhap_kho_model import NhapKhoModel
from main.models.xuat_kho_model import XuatKhoModel


def calculate_gia_goc_xuat_kho(pn_13, xuat_kho_id=None, calculate_date=datetime.now()):
    if xuat_kho_id:
        so_far_xuat_kho = XuatKhoModel.objects.filter(
            pn_13=pn_13, input_date__lte=calculate_date).exclude(id=xuat_kho_id)
    else:
        so_far_xuat_kho = XuatKhoModel.objects.filter(
            pn_13=pn_13, input_date__lte=calculate_date)

    if so_far_xuat_kho:
        recent_xuat_kho = so_far_xuat_kho.last()
        nhap_kho_till_recent_xuat_kho = \
            NhapKhoModel.objects.filter(pn_13=pn_13, input_date__lte=recent_xuat_kho.input_date)
        nhap_kho_after_recent_xuat_kho = \
            NhapKhoModel.objects.filter(pn_13=pn_13, input_date__gt=recent_xuat_kho.input_date)

        # Weighted average
        total_nhap = sum([nhap_kho.quantity for nhap_kho in nhap_kho_till_recent_xuat_kho])
        total_xuat = sum([xuat_kho.quantity for xuat_kho in so_far_xuat_kho])
        current_ton_kho = total_nhap - total_xuat

        total_price = current_ton_kho * recent_xuat_kho.gia_goc + sum([nk.quantity * nk.gia_goc for nk in nhap_kho_after_recent_xuat_kho])
        total_amount = current_ton_kho + sum([nk.quantity for nk in nhap_kho_after_recent_xuat_kho])

        weighted_average_price = total_price / total_amount

    else:
        nhap_kho_till_recent_xuat_kho = \
            NhapKhoModel.objects.filter(pn_13=pn_13, input_date__lte=calculate_date)
        if not nhap_kho_till_recent_xuat_kho:
            return 0

        # Weighted average
        total_price = sum([nk.quantity * nk.gia_goc for nk in nhap_kho_till_recent_xuat_kho])
        total_amount = sum([nk.quantity for nk in nhap_kho_till_recent_xuat_kho])
        weighted_average_price = total_price / total_amount
    return round(weighted_average_price, 2)
