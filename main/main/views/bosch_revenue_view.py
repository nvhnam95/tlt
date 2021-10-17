from rest_framework.viewsets import ModelViewSet

from main.models.bosch_revenue_model import BoschRevenueModel
from main.models.cost_model import CostModel
from main.models.po_model import POModel
from main.serializers.bosch_revenue_ser import BoschRevenueSerializer
from main.serializers.cost_ser import CostSerializer
from main.serializers.po_ser import POSerializer
from django_filters.rest_framework import DjangoFilterBackend

from main.utils.xuat_nhap_ton_service import refresh_xnt


class BoschRevenueView(ModelViewSet):
    serializer_class = BoschRevenueSerializer
    queryset = BoschRevenueModel.objects.all()
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        start = self.request.query_params.get('start')
        end = self.request.query_params.get('end')
        if start and end:
            queryset = BoschRevenueModel.objects.filter(date__range=[start, end])
        else:
            queryset = super().get_queryset()
        return queryset
