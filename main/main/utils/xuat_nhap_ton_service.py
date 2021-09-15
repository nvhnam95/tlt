from main.models.nhap_kho_model import NhapKhoModel
from main.models.po_model import POModel
from main.models.xuat_kho_model import XuatKhoModel
from main.models.xuat_nhap_ton_model import XuatNhapTonModel


def update_xnt_after_nhap_kho(nhap_kho_obj):
    pn_13 = nhap_kho_obj.pn_13
    xnts = XuatNhapTonModel.objects.filter(pn_13=pn_13)

    so_luong_nhap = 0
    so_luong_xuat = 0
    total_po = 0
    dap_price = nhap_kho_obj.dap_price

    if xnts:
        xnt = xnts.first()
    else:
        xnt = XuatNhapTonModel()

    xnt.pn_13 = nhap_kho_obj.pn_13
    xnt.bosch_no = nhap_kho_obj.bosch_no
    xnt.z_exel_no = nhap_kho_obj.z_exel_no
    xnt.stamping = nhap_kho_obj.stamping
    xnt.english_des = nhap_kho_obj.english_des
    xnt.app_des = nhap_kho_obj.app_des
    xnt.dap_price = nhap_kho_obj.dap_price

    all_phieu_nhap_kho = NhapKhoModel.objects.filter(pn_13=pn_13)
    for pnk in all_phieu_nhap_kho:
        so_luong_nhap += pnk.quantity

    all_phieu_xuat_kho = XuatKhoModel.objects.filter(pn_13=pn_13)
    for pxk in all_phieu_xuat_kho:
        so_luong_xuat += pxk.quantity

    all_po = POModel.objects.filter(pn_13=pn_13)
    for po in all_po:
        total_po += po.quantity

    ton_cuoi = so_luong_nhap - so_luong_xuat
    bor = total_po - so_luong_nhap
    bor_price = dap_price * bor

    xnt.so_luong_nhap = so_luong_nhap
    xnt.so_luong_xuat = so_luong_xuat
    xnt.ton_cuoi = ton_cuoi
    xnt.total_po = total_po
    xnt.bor = bor
    xnt.bor_price = bor_price
    xnt.save()


def update_xnt_after_xuat_kho(xuat_kho_obj):
    pn_13 = xuat_kho_obj.pn_13
    xnts = XuatNhapTonModel.objects.filter(pn_13=pn_13)

    so_luong_xuat = 0

    if xnts:
        xnt = xnts.first()
    else:
        return

    so_luong_nhap = xnt.so_luong_nhap
    all_phieu_xuat_kho = XuatKhoModel.objects.filter(pn_13=pn_13)
    for pxk in all_phieu_xuat_kho:
        so_luong_xuat += pxk.quantity

    ton_cuoi = so_luong_nhap - so_luong_xuat

    xnt.so_luong_xuat = so_luong_xuat
    xnt.ton_cuoi = ton_cuoi
    xnt.save()


def update_xnt_after_create_po(xuat_kho_obj):
    pn_13 = xuat_kho_obj.pn_13
    xnts = XuatNhapTonModel.objects.filter(pn_13=pn_13)

    so_luong_xuat = 0
    total_po = 0

    if xnts:
        xnt = xnts.first()
    else:
        return

    so_luong_nhap = xnt.so_luong_nhap
    all_phieu_xuat_kho = XuatKhoModel.objects.filter(pn_13=pn_13)
    for pxk in all_phieu_xuat_kho:
        so_luong_xuat += pxk.quantity

    all_po = POModel.objects.filter(pn_13=pn_13)
    for po in all_po:
        total_po += po.quantity

    dap_price = xnt.dap_price
    bor = total_po - so_luong_nhap
    bor_price = dap_price * bor
    xnt.total_po = total_po
    xnt.bor = bor
    xnt.bor_price = bor_price
    xnt.save()
