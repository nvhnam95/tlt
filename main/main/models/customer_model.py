from django.db import models


class CustomerModel(models.Model):
    code = models.TextField(null=True, blank=True, )
    name = models.TextField(default='', blank=True)
