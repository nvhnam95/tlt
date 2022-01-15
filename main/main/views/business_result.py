from rest_framework.response import Response
from rest_framework.views import APIView

from main.models.bosch_revenue_model import BoschRevenueModel
from main.models.cong_no_models import CongNoModel, CongNoPaymentModel
from main.models.cost_model import CostModel
from main.models.nhap_kho_model import NhapKhoModel
from main.models.po_model import POModel
from main.models.side_revenue_model import SideRevenueModel
from main.models.xuat_kho_model import XuatKhoModel


class BusinessResultView(APIView):

    def get(self, request):
        import time
        time.sleep(0.05)
        start = request.query_params.get("start")
        end = request.query_params.get("end")

        # New req: dont filter cong_no_chua_thu at all
        tong_tien_no_all = sum([x.total for x in CongNoModel.objects.all()])
        tong_tien_da_thu_all = sum([x.amount for x in CongNoPaymentModel.objects.all()])
        cong_no_chua_thu_all = tong_tien_no_all - tong_tien_da_thu_all

        tong_gia_goc_all = sum([x.tong_gia_goc for x in NhapKhoModel.objects.all()])
        tong_tien_goc_all = sum([x.tien_goc for x in XuatKhoModel.objects.all()])

        if start and end:
            doanh_thu_bosch = sum([x.total for x in BoschRevenueModel.objects.filter(date__range=[start, end])])
            doanh_thu_ngoai = sum([x.tien_ban for x in SideRevenueModel.objects.filter(date__range=[start, end])])
            tong_gia_tri_von_goc = sum([x.tien_goc for x in XuatKhoModel.objects.filter(input_date__range=[start, end])])
            chi_phi_ban_hang = sum([x.value for x in CostModel.objects.filter(date__range=[start, end], cost_type="CPBANHANG")])
            chi_phi_quan_ly = sum([x.value for x in CostModel.objects.filter(date__range=[start, end], cost_type="CPQUANLY")])
            chi_phi_khac = sum([x.value for x in CostModel.objects.filter(date__range=[start, end], cost_type="CPKHAC")])
            tong_extension_price = sum([x.extension_price for x in POModel.objects.filter(updated_on__range=[start, end])])

            tong_gia_goc = sum([x.tong_gia_goc for x in NhapKhoModel.objects.filter(input_date__range=[start, end])])
            tong_tien_goc = sum([x.tien_goc for x in XuatKhoModel.objects.filter(input_date__range=[start, end])])

            # Cong no chua thu
            tong_tien_no = sum([x.total for x in CongNoModel.objects.filter(ngay_xuat_hang__range=[start, end])])
            tong_tien_da_thu = sum([x.amount for x in CongNoPaymentModel.objects.filter(date__range=[start, end])])

            cong_no_chua_thu = tong_tien_no - tong_tien_da_thu

        else:
            doanh_thu_bosch = sum([x.total for x in BoschRevenueModel.objects.all()])
            doanh_thu_ngoai = sum([x.tien_ban for x in SideRevenueModel.objects.all()])
            tong_gia_tri_von_goc = sum([x.tien_goc for x in XuatKhoModel.objects.all()])
            chi_phi_ban_hang = sum(
                [x.value for x in CostModel.objects.filter(cost_type="CPBANHANG")])
            chi_phi_quan_ly = sum(
                [x.value for x in CostModel.objects.filter(cost_type="CPQUANLY")])
            chi_phi_khac = sum([x.value for x in CostModel.objects.filter(cost_type="CPKHAC")])
            tong_extension_price = sum(
                [x.extension_price for x in POModel.objects.all()])
            tong_gia_goc = sum([x.tong_gia_goc for x in NhapKhoModel.objects.all()])
            tong_tien_goc = sum([x.tien_goc for x in XuatKhoModel.objects.all()])

            # Cong no chua thu
            tong_tien_no = sum([x.total for x in CongNoModel.objects.all()])
            tong_tien_da_thu = sum([x.amount for x in CongNoPaymentModel.objects.all()])

            cong_no_chua_thu = tong_tien_no - tong_tien_da_thu
        data = [
            {
                "no": 1,
                "content": "Doanh thu bán hàng Bosch",
                "value": doanh_thu_bosch
            },
            {
                "no": 2,
                "content": "Các khoản giảm trừ doanh thu",
                "value": ""
            },
            {
                "no": 3,
                "content": "Doanh thu thuần về bán hàng và cung cấp dịch vụ (10 = 01 - 02)",
                "value": ""
            },
            {
                "no": 4,
                "content": "Tổng Giá trị vốn gốc",
                "value": tong_gia_tri_von_goc
            },
            {
                "no": 5,
                "content": "Lợi nhuận bán hàng Bosch",
                "value": doanh_thu_bosch - tong_gia_tri_von_goc
            },
            {
                "no": 6,
                "content": "Doanh thu hoạt động tài chính",
                "value": ""
            },
            {
                "no": 7,
                "content": "Chi phí tài chính",
                "value": ""
            },
            {
                "no": 8,
                "content": "Chi phí bán hàng",
                "value": chi_phi_ban_hang
            },
            {
                "no": 9,
                "content": "Chi phí quản lý",
                "value": chi_phi_quan_ly
            },
            {
                "no": 11,
                "content": "Doanh Thu ngoài",
                "value": doanh_thu_ngoai
            },
            {
                "no": 12,
                "content": "Chi Phí Khác",
                "value": chi_phi_khac
            },
            {
                "no": 14,
                "content": "Tổng lợi nhuận kế toán trước thuế",
                "value": doanh_thu_bosch - tong_gia_tri_von_goc + doanh_thu_ngoai - chi_phi_ban_hang - chi_phi_quan_ly - chi_phi_khac
            },
            {
                "no": 15,
                "content": " Chi phí thuế TNDN hiện hành",
                "value": ""
            },
            {
                "no": 16,
                "content": "Chi phí thuế TNDN hoãn lại",
                "value": ""
            },
            {
                "no": 17,
                "content": "Lợi nhuận sau thuế TNDN (60=50-51-52)",
                "value": ""
            },
            {
                "no": 18,
                "content": "Lãi cơ bản trên cổ phiếu",
                "value": ""
            },
            {
                "no": 19,
                "content": "Lãi suy giảm trên cổ phiếu",
                "value": ""
            },
            {
                "no": "",
                "content": "Vốn đầu tư",
                "value": ""
            },
            {
                "no": "",
                "content": "Công nợ chưa thu khách hàng",
                "value": cong_no_chua_thu
            },
            {
                "no": "",
                "content": "Công nợ chưa thu toàn thời gian",
                "value": cong_no_chua_thu_all
            },
            {
                "no": "",
                "content": "Tổng giá trị đặt hàng (PO)",
                "value": tong_extension_price
            },
            {
                "no": "",
                "content": "Tổng giá trị nhập kho",
                "value": tong_gia_goc
            },
            {
                "no": "",
                "content": "Tổng Giá Trị Gốc Tồn Kho",
                "value": tong_gia_goc - tong_tien_goc
            },
            {
                "no": "",
                "content": "Tổng Giá Trị Gốc Tồn Kho Toàn Thời Gian",
                "value": tong_gia_goc_all - tong_tien_goc_all
            },
        ]
        return Response(data)
