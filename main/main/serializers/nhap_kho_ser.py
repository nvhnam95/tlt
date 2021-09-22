from rest_framework import serializers

from main.models.nhap_kho_model import NhapKhoModel
from main.utils.xuat_nhap_ton_service import refresh_xnt


class NhapKhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NhapKhoModel
        fields = "__all__"

    def create(self, validated_data):
        nhap_kho_obj = super().create(validated_data)
        refresh_xnt(nhap_kho_obj.pn_13)
        return nhap_kho_obj

    def update(self, instance, validated_data):
        nhap_kho_obj = super().update(instance, validated_data)
        refresh_xnt(nhap_kho_obj.pn_13)
        return nhap_kho_obj
