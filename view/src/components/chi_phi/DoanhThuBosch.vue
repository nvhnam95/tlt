<template>
<div>
  <DataTable
  :title=title
  :column_names=column_names
  :columns=column_definitions
  :total_data_from_parent=total_data
  :resource_url_from_parent=resource_url
  :form_name_from_parent=form_name
  :modal_name_from_parent=modal_name
  :resource_filter_from_parent=resource_filter
  :export_file_name_from_parent=export_file_name
  />
</div>

</template>

<script>

import DataTable from "../BaseTable.vue"
import moment from "moment";
import $ from "jquery";

export default {
  components: {
    DataTable,
  },
    data: function () {
    return {
      title: "Doanh Thu Bosch",
      column_names: ["Ngày", "Mã Khách Hàng", "Mã Hàng", "Số Lượng", "Giá Bán", "Thành Tiền", ""],
      column_definitions: [
        { data: "date",
          render: function(data){return moment(data).format("DD/MM/YYYY");}
        },
        { data: "client_code" },
        { data: "product_code" },
        { data: "quantity" },
        { data: "price", render: $.fn.dataTable.render.number(",", ".", 2) },
        { data: "total", render: $.fn.dataTable.render.number(",", ".", 2) },
        {
          data: null,
          width: 100,
          defaultContent:
            '<button type="button"  action="edit"  class="btn btn-warning flat ">Sửa</button>\
            <button type="button"  action="delete" class="btn btn-danger flat ">Xóa</button>',
        },
      ],
      total_data: [
        {
          "name": "Tổng Tiền",
          "column_index": 5,
          "value": 0,
          "suffix": "đồng"
        }
      ],
      resource_url: process.env.VUE_APP_API_ENDPOINT + "/api/v1/bosch-revenues",
      resource_filter: {},
      form_name: "DoanhThuBoschForm",
      modal_name: "modal-bosch-revenues-form",
      export_file_name: "doanh_thu_bosch_" + moment().format("DD_MM_YYYY"),
    }
  }
}
</script>
