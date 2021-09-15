from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from main.models.nhap_kho_model import NhapKhoModel
from main.serializers.nhap_kho_ser import NhapKhoSerializer


class NhapKhoView(ModelViewSet):
    serializer_class = NhapKhoSerializer
    queryset = NhapKhoModel.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['pn_13']
