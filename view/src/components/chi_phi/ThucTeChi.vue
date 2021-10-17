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
      title: "Thực Tế Chi",
      column_names: ["Ngày", "Nghiệp Vụ", "Mã Khách Hàng", "Nội Dung", "Số Tiền", ""],
      column_definitions: [
        { data: "date",
          render: function(data){return moment(data).format("DD/MM/YYYY");}
        },
        { data: "major" },
        { data: "client_code" },
        { data: "content" },
        { data: "value", render: $.fn.dataTable.render.number(",", ".", 2) },
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
          "column_index": 4,
          "value": 0,
          "suffix": "đồng"
        }
      ],
      resource_url: process.env.VUE_APP_API_ENDPOINT + "/api/v1/costs?cost_type=THUCTECHI",
      resource_filter: {cost_type: "THUCTECHI"},
      form_name: "ChiPhiForm",
      modal_name: "modal-thuc-te-chi-form",
      export_file_name: "thuc_te_chi_" + moment().format("DD_MM_YYYY"),
    }
  }
}
</script>
