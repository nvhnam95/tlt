from rest_framework.viewsets import ModelViewSet

from main.models.po_model import POModel
from main.serializers.po_ser import POSerializer
from django_filters.rest_framework import DjangoFilterBackend


class POView(ModelViewSet):
    serializer_class = POSerializer
    queryset = POModel.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['pn_10']
