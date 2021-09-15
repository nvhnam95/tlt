from rest_framework import serializers

from main.models.po_model import POModel
from main.utils.xuat_nhap_ton_service import update_xnt_after_create_po


class POSerializer(serializers.ModelSerializer):

    class Meta:
        model = POModel
        fields = "__all__"

    def create(self, validated_data):
        po = super().create(validated_data)
        update_xnt_after_create_po(po)
        return po
