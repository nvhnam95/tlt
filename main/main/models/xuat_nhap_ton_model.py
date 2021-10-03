from django.db import models


class XuatNhapTonModel(models.Model):
    ung_dung = models.TextField(default='', blank=True)
    pn_13 = models.TextField(default='', blank=True)
    bosch_no = models.TextField(default='', blank=True)
    z_exel_no = models.TextField(default='', blank=True)
    stamping = models.TextField(default='', blank=True)
    english_des = models.TextField(default='', blank=True)
    import_des = models.TextField(default='', blank=True)
    app_des = models.TextField(default='', blank=True)
    dap_price = models.FloatField(default=0, blank=True)
    so_luong_nhap = models.IntegerField(default=0, null=True)
    so_luong_xuat = models.IntegerField(default=0, null=True)
    ton_cuoi = models.IntegerField(default=0, null=True)
    total_po = models.IntegerField(default=0, null=True)
    bor = models.IntegerField(default=0, null=True)
    bor_price = models.FloatField(default=0, blank=True)
    gia_si = models.FloatField(default=0, blank=True)
    gia_le = models.FloatField(default=0, blank=True)
    updated_on = models.DateField(auto_now_add=True)
