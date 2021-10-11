from datetime import datetime

from django.http import HttpResponse
from openpyxl import load_workbook
import re

from main.models.nhap_kho_model import NhapKhoModel
from main.models.po_model import POModel
from main.models.xuat_kho_model import XuatKhoModel
from main.serializers.nhap_kho_ser import NhapKhoSerializer
from main.serializers.po_ser import POSerializer
from main.serializers.xuat_kho_ser import XuatKhoSerializer
from main.utils.pricing_service import calculate_gia_goc_xuat_kho

total = 0

def generate_test_data(request):
    loc = "main/utils/test/data_1.xlsx"
    global total
    # To open Workbook
    wb = load_workbook(loc, data_only=True)

    if not POModel.objects.all():
        # PO
        sheet_obj = wb.worksheets[0]
        row = 7
        while True:
            pn_13 = sheet_obj.cell(row=row, column=2).value
            if not pn_13:
                break
            validated_data = {
                "po_no": sheet_obj.cell(row=row, column=1).value or '',
                "pn_13": sheet_obj.cell(row=row, column=2).value or '',
                "pn_10": sheet_obj.cell(row=row, column=3).value or '',
                "bosch_no": sheet_obj.cell(row=row, column=4).value or '',
                "z_exel_no": sheet_obj.cell(row=row, column=5).value or '',
                "stamping": sheet_obj.cell(row=row, column=6).value or '',
                "country": sheet_obj.cell(row=row, column=7).value or '',
                "english_des": sheet_obj.cell(row=row, column=8).value or '',
                "import_des": sheet_obj.cell(row=row, column=9).value or '',
                "app_des": sheet_obj.cell(row=row, column=10).value or '',
                "quantity": sheet_obj.cell(row=row, column=11).value or 0,
                "dap_price": round(sheet_obj.cell(row=row, column=12).value or 0, 3),
                "extension_price": round(sheet_obj.cell(row=row, column=13).value or 0, 3),
                "tax": round(sheet_obj.cell(row=row, column=14).value or 0, 3),
                "gia_von": round(sheet_obj.cell(row=row, column=15).value or 0, 3),
                "gia_si": round(sheet_obj.cell(row=row, column=16).value or 0, 3),
                "gia_le": round(sheet_obj.cell(row=row, column=17).value or 0, 3),
                "lead_time": sheet_obj.cell(row=row, column=18).value or '',
                "customer": sheet_obj.cell(row=row, column=19).value or '',
                "remarks": sheet_obj.cell(row=row, column=20).value or '',
            }
            if not validated_data["gia_le"]:
                validated_data["gia_le"] = validated_data["gia_si"] * 1.1
            POSerializer().create(validated_data)
            row += 1

    if not NhapKhoModel.objects.all():
        # Nhap kho
        sheet_obj = wb.worksheets[1]
        row = 4
        while True:
            pn_13 = sheet_obj.cell(row=row, column=4).value
            if not pn_13:
                break
            input_date = None
            cell_value = sheet_obj.cell(row=row, column=1).value
            if type(cell_value) == datetime:
                input_date = cell_value.strftime("%Y-%m-%d")
            validated_data = {
                "input_date": input_date,
                "license_no": sheet_obj.cell(row=row, column=2).value or '',
                "provider": sheet_obj.cell(row=row, column=3).value or '',
                "pn_13": sheet_obj.cell(row=row, column=4).value or '',
                "pn_10": sheet_obj.cell(row=row, column=5).value or '',
                "bosch_no": sheet_obj.cell(row=row, column=6).value or '',
                "z_exel_no": sheet_obj.cell(row=row, column=7).value or '',
                "stamping": sheet_obj.cell(row=row, column=8).value or '',
                "gia_von": sheet_obj.cell(row=row, column=11).value or 0,
                "gia_si": sheet_obj.cell(row=row, column=12).value or 0,
                "gia_le": sheet_obj.cell(row=row, column=13).value or 0,
                "quantity": sheet_obj.cell(row=row, column=14).value or 0,
                "dap_price": round(float(sheet_obj.cell(row=row, column=15).value or 0), 3),
                "extension_price": round(sheet_obj.cell(row=row, column=16).value or 0, 3),
                "ratio": sheet_obj.cell(row=row, column=17).value or 0,
                "tax": float(sheet_obj.cell(row=row, column=18).value or 0),
                "vat_percentage":  int(re.search(r'\d+', sheet_obj.cell(row=row, column=19).value or 0).group()),
                "po_no": sheet_obj.cell(row=row, column=20).value or '',
            }
            validated_data["gia_goc"] = round(validated_data["dap_price"] * validated_data["ratio"] * validated_data["tax"], 3)
            validated_data["tong_gia_goc"] = round(validated_data["gia_goc"] * validated_data["quantity"], 3)
            if not validated_data["gia_le"]:
                validated_data["gia_le"] = validated_data["gia_si"] * 1.1

            recent_po = POModel.objects.filter(pn_13=validated_data["pn_13"]).last()
            if recent_po:
                validated_data["english_des"] = recent_po.english_des
                validated_data["app_des"] = recent_po.app_des
                validated_data["import_des"] = recent_po.import_des
            NhapKhoSerializer().create(validated_data)
            row += 1

    if not XuatKhoModel.objects.all():
        # Xuat kho
        sheet_obj = wb.worksheets[2]
        row = 8
        while True:
            pn_13 = sheet_obj.cell(row=row, column=3).value or ''
            if not pn_13:
                break
            input_date = sheet_obj.cell(row=row, column=2).value
            if input_date:
                input_date = input_date.strftime("%Y-%m-%d")


            if pn_13 == "0445020126391":
                pass
            validated_data = {
                "input_date": input_date,
                "pn_13": pn_13,
                "quantity": sheet_obj.cell(row=row, column=6).value or '',
            }
            last_nhap_kho = NhapKhoModel.objects.filter(pn_13=validated_data["pn_13"]).last()
            if last_nhap_kho:
                validated_data["gia_goc"] = calculate_gia_goc_xuat_kho(pn_13=pn_13, calculate_date=input_date)
                validated_data["gia_si"] = last_nhap_kho.gia_si
                validated_data["gia_le"] = last_nhap_kho.gia_le
                validated_data["english_des"] = last_nhap_kho.english_des
                validated_data["import_des"] = last_nhap_kho.import_des
                validated_data["app_des"] = last_nhap_kho.app_des
                validated_data["tien_goc"] = round(validated_data["gia_goc"] * validated_data["quantity"], 3)
                validated_data["customer"] = ""

            XuatKhoSerializer().create(validated_data)
            row += 1

    return HttpResponse("Done")
