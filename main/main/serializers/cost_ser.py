from rest_framework import serializers

from main.models.cost_model import CostModel


class CostSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostModel
        exclude = []
