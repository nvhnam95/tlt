import io

import xlsxwriter
from django.http import HttpResponse
from rest_framework.decorators import api_view


@api_view(['post'])
def json_to_excel(request):
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()
    data = request.data

    for row_num, columns in enumerate(data):
        for col_num, cell_data in enumerate(columns):
            worksheet.write(row_num, col_num, cell_data)

    workbook.close()

    output.seek(0)

    response = HttpResponse(
        output,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )

    return response
