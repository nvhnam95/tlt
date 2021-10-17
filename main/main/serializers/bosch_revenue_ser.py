from rest_framework import serializers

from main.models.bosch_revenue_model import BoschRevenueModel
from main.models.xuat_kho_model import XuatKhoModel
from main.utils.xuat_nhap_ton_service import refresh_xnt


class BoschRevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoschRevenueModel
        fields = "__all__"
