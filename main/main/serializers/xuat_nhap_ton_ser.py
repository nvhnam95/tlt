from rest_framework import serializers

from main.models.xuat_nhap_ton_model import XuatNhapTonModel


class XuatNhapTonSerializer(serializers.ModelSerializer):
    class Meta:
        model = XuatNhapTonModel
        fields = "__all__"
