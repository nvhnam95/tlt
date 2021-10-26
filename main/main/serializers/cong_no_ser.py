from rest_framework import serializers

from main.models.cong_no_models import CongNoModel


class CongNoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CongNoModel
        fields = "__all__"
