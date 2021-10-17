from django.db import models


class CostModel(models.Model):
    date = models.DateField(null=True, blank=True, )
    major = models.TextField(default='', blank=True)
    client_code = models.TextField(default='', blank=True)
    content = models.TextField(default='', blank=True)
    value = models.FloatField(default=0, blank=True)
    cost_type = models.TextField(default='')  # chi phi ban hang, chi phi quan ly, chi phi khac, thuc te chi
    updated_on = models.DateField(auto_now_add=True)
