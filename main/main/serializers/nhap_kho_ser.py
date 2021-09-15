from rest_framework import serializers

from main.models.nhap_kho_model import NhapKhoModel
from main.utils.xuat_nhap_ton_service import update_xnt_after_nhap_kho


class NhapKhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NhapKhoModel
        fields = "__all__"

    def create(self, validated_data):
        nhap_kho = super().create(validated_data)
        update_xnt_after_nhap_kho(nhap_kho)
        return nhap_kho
