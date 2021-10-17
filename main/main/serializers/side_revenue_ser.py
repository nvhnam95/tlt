from rest_framework import serializers

from main.models.side_revenue_model import SideRevenueModel


class SideRevenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = SideRevenueModel
        fields = "__all__"
