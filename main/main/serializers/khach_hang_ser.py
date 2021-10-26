from rest_framework import serializers

from main.models.cong_no_models import CongNoKhachHangModel


class CongNoKhachHangSerializer(serializers.ModelSerializer):
    class Meta:
        model = CongNoKhachHangModel
        fields = "__all__"
