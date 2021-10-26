from django.db import models


class CongNoKhachHangModel(models.Model):
    name = models.TextField(default='', blank=True)
    company = models.TextField(default='', blank=True)
    address = models.TextField(default='', blank=True)
    note = models.TextField(default='', blank=True)
    ma_so_thue = models.TextField(default='', blank=True)


class CongNoModel(models.Model):
    ngay_xuat_hang = models.DateField(null=True, blank=True)
    bosch_no = models.TextField(default='', blank=True)
    zexel_no = models.TextField(default='', blank=True)
    ma_tem = models.TextField(default='', blank=True)
    english_name = models.TextField(default='', blank=True)
    vietnamese_name = models.TextField(default='', blank=True)
    quantity = models.IntegerField(default=0, null=True)
    price = models.FloatField(default=0, null=True)
    total = models.FloatField(default=0, null=True)
    vat = models.FloatField(default=0, null=True)
    khach_hang = models.ForeignKey(CongNoKhachHangModel, on_delete=models.CASCADE)


class CongNoPaymentModel(models.Model):
    date = models.DateField(null=True, blank=True)
    amount = models.FloatField(default=0, null=True)
    note = models.TextField(default='', blank=True)
    khach_hang = models.ForeignKey(CongNoKhachHangModel, on_delete=models.CASCADE)
