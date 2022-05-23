from django.urls import path
from rest_framework.routers import DefaultRouter

# from main.models.page_access_model import PageAccessModel
from main.utils.data.data_generator import generate_test_data
from main.views.auth_views import user_detail
from main.views.bosch_revenue_view import BoschRevenueView
from main.views.business_result import BusinessResultView
from main.views.cong_no_payment_view import CongNoPaymentView
from main.views.cong_no_khach_hang_view import CongNoKhachHangView
from main.views.cong_no_view import CongNoView
from main.views.cost_view import CostView
from main.views.customer_view import CustomerView
from main.views.nhap_kho_view import NhapKhoView
from main.views.po_view import POView
from main.views.side_revenue_view import SideRevenueView
from main.views.tools import json_to_excel
from main.views.user_view import UserView
from main.views.xuat_kho_view import XuatKhoView
from main.views.xuat_nhap_ton_view import XuatNhapTonView
from rest_framework.authtoken import views

router = DefaultRouter(trailing_slash=False)
router.register(r'api/v1/purchasing-orders', POView)
router.register(r'api/v1/nhap-kho', NhapKhoView)
router.register(r'api/v1/xuat-kho', XuatKhoView)
router.register(r'api/v1/xuat-nhap-ton', XuatNhapTonView)
router.register(r'api/v1/costs', CostView)
router.register(r'api/v1/bosch-revenues', BoschRevenueView)
router.register(r'api/v1/side-revenues', SideRevenueView)
router.register(r'api/v1/customers', CustomerView)
router.register(r'api/v1/users', UserView)

# --- Cong no ---
router.register(r'api/v1/cong-no', CongNoView)
router.register(r'api/v1/cong-no-khach-hang', CongNoKhachHangView)
router.register(r'api/v1/cong-no-payment', CongNoPaymentView)

urlpatterns = [
    path('give-me-some-test-data', generate_test_data),
    path('api/v1/tools/to-xlsx', json_to_excel),
    path('api/v1/business-results', BusinessResultView.as_view()),
    path('api/v1/current-user', user_detail),
    path('api-token-auth/', views.obtain_auth_token)
]

urlpatterns += router.urls
