from rest_framework import serializers

from main.models.xuat_kho_model import XuatKhoModel
from main.utils.xuat_nhap_ton_service import update_xnt_after_xuat_kho


class XuatKhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = XuatKhoModel
        fields = "__all__"

    def create(self, validated_data):
        xuat_kho = super().create(validated_data)
        update_xnt_after_xuat_kho(xuat_kho)
        return xuat_kho
