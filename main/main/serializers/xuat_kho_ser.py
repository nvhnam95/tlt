from rest_framework import serializers

from main.models.xuat_kho_model import XuatKhoModel
from main.utils.xuat_nhap_ton_service import refresh_xnt


class XuatKhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = XuatKhoModel
        fields = "__all__"

    def create(self, validated_data):
        xuat_kho_obj = super().create(validated_data)
        refresh_xnt(xuat_kho_obj.pn_13)
        return xuat_kho_obj

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        refresh_xnt(instance.pn_13)
        return instance
