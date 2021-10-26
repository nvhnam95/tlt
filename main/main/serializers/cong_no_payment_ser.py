from rest_framework import serializers

from main.models.cong_no_models import CongNoPaymentModel


class CongNoPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CongNoPaymentModel
        exclude = []
