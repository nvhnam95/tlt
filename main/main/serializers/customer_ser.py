from rest_framework import serializers

from main.models.customer_model import CustomerModel


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerModel
        exclude = []
