import io
from xlsxwriter.utility import xl_rowcol_to_cell
import xlsxwriter
from django.http import HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from main.models.cong_no_models import CongNoModel, CongNoKhachHangModel, CongNoPaymentModel
from main.serializers.cong_no_ser import CongNoSerializer


class CongNoView(ModelViewSet):
    serializer_class = CongNoSerializer
    queryset = CongNoModel.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["khach_hang"]

    def get_queryset(self):
        return super().get_queryset().order_by("-ngay_xuat_hang")

    @action(['get'], False, 'export-excel')
    def calculate_gia_goc(self, request):
        khach_hang_id = request.query_params.get('khach_hang_id')
        khach_hang = CongNoKhachHangModel.objects.get(id=khach_hang_id)
        cong_no = CongNoModel.objects.filter(khach_hang=khach_hang).order_by("-ngay_xuat_hang")
        payments = CongNoPaymentModel.objects.filter(khach_hang=khach_hang).order_by("-date")

        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet()

        currency_format = workbook.add_format({'num_format': '#,##0.00'})
        red_bold_format = workbook.add_format({'bold': True, 'font_color': 'red'})
        red_bold_currency_format = workbook.add_format({'num_format': '#,##0.00', 'bold': True, 'font_color': 'red'})
        bold_format = workbook.add_format({'bold': True})

        cong_no_column = ["Ngày xuất hàng", "Mã Bosch",	"Mã Zexel",	"Mã tem trên hộp", "Tên Tiếng Anh", "Tên Tiếng Việt", "Số Lượng", "VAT", "Đơn giá", "Thành Tiền"]
        # for row_num, columns in enumerate(data):
        #     for col_num, cell_data in enumerate(columns):
        #         worksheet.write(row_num, col_num, cell_data)

        worksheet.write(0, 0, "From", bold_format)
        worksheet.write(0, 1, "TLT INTERNATIONAL ENGINEERING TECHNOLOGY CO.,LTD", )

        worksheet.write(1, 0, "To", bold_format)
        worksheet.write(1, 1, khach_hang.name, )

        worksheet.write(2, 0, "Address", bold_format)
        worksheet.write(2, 1, khach_hang.address, )

        worksheet.write(3, 0, "Company", bold_format)
        worksheet.write(3, 1, khach_hang.company, )

        worksheet.write(4, 0, "Mã số thuế", bold_format)
        worksheet.write(4, 1, khach_hang.ma_so_thue, )

        worksheet.write(5, 0, "Note", bold_format)
        worksheet.write(5, 1, khach_hang.note, )

        current_row = 6
        for i, d in enumerate(cong_no_column):
            worksheet.write(current_row, i + 1, d, bold_format)

        current_row += 1
        start_sum_cong_no = xl_rowcol_to_cell(current_row, 10)

        to_merge_cell_list = []

        cong_no_dict = {}

        for c in cong_no:
            current_month = c.ngay_xuat_hang.month
            current_year = c.ngay_xuat_hang.year
            k = f"{current_month}/{current_year}"
            if k in cong_no_dict:
                cong_no_dict[k].append(c)
            else:
                cong_no_dict[k] = [c]

        for month_year in cong_no_dict:
            cong_no_list = cong_no_dict[month_year]
            merge_from = merge_to = current_row
            for c in cong_no_list:
                worksheet.write(current_row, 1, c.ngay_xuat_hang.strftime("%d/%m/%Y"))
                worksheet.write(current_row, 2, c.bosch_no)
                worksheet.write(current_row, 3, c.zexel_no)
                worksheet.write(current_row, 4, c.ma_tem)
                worksheet.write(current_row, 5, c.english_name)
                worksheet.write(current_row, 6, c.vietnamese_name)
                worksheet.write(current_row, 7, c.quantity)
                worksheet.write(current_row, 8, c.vat)
                worksheet.write(current_row, 9, c.price, currency_format)
                worksheet.write(current_row, 10, c.total, currency_format)
                merge_to = current_row
                current_row += 1

            to_merge_cell_list.append({"from": xl_rowcol_to_cell(merge_from, 0),
                                       "to": xl_rowcol_to_cell(merge_to, 0),
                                       "val": f'Tháng {month_year}'})

        end_sum_cong_no = xl_rowcol_to_cell(current_row-1, 10)
        worksheet.write(current_row, 9, "Tổng số tiền nợ", red_bold_format)
        worksheet.write_formula(current_row, 10, f"=SUM({start_sum_cong_no}:{end_sum_cong_no})", red_bold_currency_format)
        tong_tien_no_cell = xl_rowcol_to_cell(current_row, 10)

        current_row += 2
        worksheet.write(current_row, 9, "Thanh toán", red_bold_format)
        current_row += 1
        start_sum_thanh_toan = xl_rowcol_to_cell(current_row, 10)
        for i in payments:
            worksheet.write(current_row, 9, i.date.strftime("%d/%m/%Y"))
            worksheet.write(current_row, 10, i.amount, currency_format)
            current_row += 1
        end_sum_thanh_toan = xl_rowcol_to_cell(current_row-1, 10)
        current_row += 1

        worksheet.write(current_row, 9, "Còn lại", red_bold_format)
        worksheet.write_formula(current_row, 10, f"={tong_tien_no_cell} - SUM({start_sum_thanh_toan}:{end_sum_thanh_toan})", red_bold_currency_format)
        for i in to_merge_cell_list:
            if i["from"] == i["to"]:
                worksheet.write(i["from"], i["val"])
            else:
                worksheet.merge_range(f'{i["from"]}:{i["to"]}', i["val"])

        worksheet.set_column(0, 0, 14)
        worksheet.set_column(1, 1, 13)
        worksheet.set_column(2, 2, max([len(c.bosch_no) for c in cong_no]) + 1)
        worksheet.set_column(3, 3, max([len(c.zexel_no) for c in cong_no]) + 1)
        worksheet.set_column(4, 4, max([len(c.ma_tem) for c in cong_no]) + 2)
        worksheet.set_column(5, 5, max([len(c.english_name) for c in cong_no]) + 1)
        worksheet.set_column(6, 6, max([len(c.vietnamese_name) for c in cong_no]) + 1)
        worksheet.set_column(7, 7, 9)
        worksheet.set_column(8, 8, max([len(str(c.vat)) for c in cong_no]) + 3)
        worksheet.set_column(9, 9, max([max([len(str(c.price)) for c in cong_no]) + 5, 16]))
        worksheet.set_column(10, 10, max([len(str(c.total)) for c in cong_no]) + 3)

        workbook.close()
        output.seek(0)
        response = HttpResponse(
            output,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        return response

