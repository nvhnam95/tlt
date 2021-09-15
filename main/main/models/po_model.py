from django.db import models


class POModel(models.Model):
    po_no = models.TextField(default='', blank=True)
    pn_13 = models.TextField(default='', blank=True)
    pn_10 = models.TextField(default='', blank=True)
    bosch_no = models.TextField(default='', blank=True)
    z_exel_no = models.TextField(default='', blank=True)
    stamping = models.TextField(default='', blank=True)
    country = models.TextField(default='', blank=True)
    english_des = models.TextField(default='', blank=True)
    import_des = models.TextField(default='', blank=True)
    app_des = models.TextField(default='', blank=True)
    quantity = models.IntegerField(default=0, null=True)
    dap_price = models.FloatField(default=0, blank=True)
    extension_price = models.FloatField(default=0, blank=True)
    tax = models.FloatField(default=0, blank=True)
    gia_von = models.FloatField(default=0, blank=True)
    gia_si = models.FloatField(default=0, blank=True)
    gia_le = models.FloatField(default=0, blank=True)
    lead_time = models.TextField(default='', blank=True)
    customer = models.TextField(default='', blank=True)
    remarks = models.TextField(default='', blank=True)
