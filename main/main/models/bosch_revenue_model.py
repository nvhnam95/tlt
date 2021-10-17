from django.db import models


class BoschRevenueModel(models.Model):
    date = models.DateField(null=True, blank=True, )
    client_code = models.TextField(default='', blank=True)
    product_code = models.TextField(default='', blank=True)
    quantity = models.IntegerField(default=0, blank=True)
    price = models.FloatField(default=0, blank=True)
    total = models.FloatField(default=0)
