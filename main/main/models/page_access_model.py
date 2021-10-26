from django.db import models


class PageAccessModel(models.Model):
    class Meta:
        managed = False
        default_permissions = ()

        permissions = (
            ('can_view_home', 'Home Page'),

            ('can_view_po', 'PO Page'),
            ('can_view_nhap_kho', 'Nhap Kho Page'),
            ('can_view_xuat_kho', 'Xuat Kho Page'),
            ('can_view_xnt', "XNT Page"),

            ('can_view_chi_phi_ban_hang', 'Chi Phi Ban Hang Page'),
            ('can_view_chi_phi_quan_ly', 'Chi Phi Quan Ly Page'),
            ('can_view_chi_phi_khac', 'Chi Phi Khac Page'),
            ('can_view_thuc_te_chi', 'Thuc Te Chi Page'),
            ('can_view_doanh_thu_bosch', 'Doanh Thu Bosch Page'),
            ('can_view_doanh_thu_ngoai', 'Doanh Thu Ngoai Page'),
            ('can_view_ket_qua_kinh_doanh', 'Ket Qua Kinh Doanh Page'),

            ('can_view_cong_no', 'Cong No Page'),
            ('can_view_khach_hang', 'Khach Hang Page'),
            ('can_view_user', 'User Page'),
        )
