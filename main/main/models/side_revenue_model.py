from django.db import models


class SideRevenueModel(models.Model):
    date = models.DateField(null=True, blank=True, )
    client_code = models.TextField(default='', blank=True)
    accessory_code = models.TextField(default='', blank=True)
    quantity = models.IntegerField(default='', blank=True)
    gia_von = models.FloatField(default=0, null=True)
    tien_von = models.FloatField(default=0, null=True)
    gia_ban = models.FloatField(default=0, null=True)
    tien_ban = models.FloatField(default=0, null=True)
    content = models.TextField(default='', blank=True)

