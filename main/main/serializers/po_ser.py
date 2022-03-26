from rest_framework import serializers

from main.models.po_model import POModel
from main.utils.xuat_nhap_ton_service import refresh_xnt


class POSerializer(serializers.ModelSerializer):

    class Meta:
        model = POModel
        fields = "__all__"

    def create(self, validated_data):
        po_obj = super().create(validated_data)
        refresh_xnt(po_obj.pn_13)
        return po_obj

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        refresh_xnt(instance.pn_13)
        return instance
