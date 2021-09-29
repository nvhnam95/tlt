from django.conf import settings
from django.db import models


class XuatKhoModel(models.Model):
    pn_13 = models.TextField(default='', blank=True)
    input_date = models.DateField(null=True, blank=True, )
    quantity = models.IntegerField(default=0, null=True)
    gia_goc = models.FloatField(default=0, blank=True)
    tien_goc = models.FloatField(default=0, blank=True)
    english_des = models.TextField(default='', blank=True)
    import_des = models.TextField(default='', blank=True)
    app_des = models.TextField(default='', blank=True)
    customer = models.TextField(default='', blank=True)
    gia_si = models.FloatField(default=0, blank=True)
    gia_le = models.FloatField(default=0, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
