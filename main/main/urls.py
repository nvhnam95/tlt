from django.urls import path
from rest_framework.routers import DefaultRouter

from main.utils.test.test_data import generate_test_data
from main.views.bosch_revenue_view import BoschRevenueView
from main.views.business_result import BusinessResultView
from main.views.cost_view import CostView
from main.views.nhap_kho_view import NhapKhoView
from main.views.po_view import POView
from main.views.side_revenue_view import SideRevenueView
from main.views.tools import json_to_excel
from main.views.xuat_kho_view import XuatKhoView
from main.views.xuat_nhap_ton_view import XuatNhapTonView

router = DefaultRouter(trailing_slash=False)
router.register(r'api/v1/purchasing-orders', POView)
router.register(r'api/v1/nhap-kho', NhapKhoView)
router.register(r'api/v1/xuat-kho', XuatKhoView)
router.register(r'api/v1/xuat-nhap-ton', XuatNhapTonView)
router.register(r'api/v1/costs', CostView)
router.register(r'api/v1/bosch-revenues', BoschRevenueView)
router.register(r'api/v1/side-revenues', SideRevenueView)

urlpatterns = [
    path('give-me-some-test-data', generate_test_data),
    path('api/v1/tools/to-xlsx', json_to_excel),
    path('api/v1/business-results', BusinessResultView.as_view()),
]

urlpatterns += router.urls
