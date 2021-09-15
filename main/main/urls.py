from rest_framework.routers import DefaultRouter

from main.views.nhap_kho_view import NhapKhoView
from main.views.po_view import POView
from main.views.xuat_kho_view import XuatKhoView
from main.views.xuat_nhap_ton_view import XuatNhapTonView

router = DefaultRouter(trailing_slash=False)
router.register(r'api/v1/purchasing-orders', POView)
router.register(r'api/v1/nhap-kho', NhapKhoView)
router.register(r'api/v1/xuat-kho', XuatKhoView)
router.register(r'api/v1/xuat-nhap-ton', XuatNhapTonView)
urlpatterns = router.urls
