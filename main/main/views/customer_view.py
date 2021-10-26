from django_filters.rest_framework import DjangoFilterBackend
from main.serializers.customer_ser import CustomerSerializer
from rest_framework.viewsets import ModelViewSet

from main.models.customer_model import CustomerModel


class CustomerView(ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = CustomerModel.objects.all()
    filter_backends = [DjangoFilterBackend]
