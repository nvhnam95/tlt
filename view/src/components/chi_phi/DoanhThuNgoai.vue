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
      title: "Doanh Thu Ngoài",
      column_names: ["Ngày", "Mã Khách Hàng", "Mã Phụ Tùng", "Số Lượng", "Giá Vốn", "Tiền Vốn", "Giá Bán", "Tiền Bán", "Nội Dung", ""],
      column_definitions: [
        { data: "date",
          render: function(data){return moment(data).format("DD/MM/YYYY");}
        },
        { data: "client_code" },
        { data: "accessory_code" },
        { data: "quantity" },
        { data: "gia_von", render: $.fn.dataTable.render.number(",", ".", 2) },
        { data: "tien_von", render: $.fn.dataTable.render.number(",", ".", 2) },
        { data: "gia_ban", render: $.fn.dataTable.render.number(",", ".", 2) },
        { data: "tien_ban", render: $.fn.dataTable.render.number(",", ".", 2) },
        { data: "content"},
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
          "column_index": 7,
          "value": 0,
          "suffix": "đồng"
        }
      ],
      resource_url: process.env.VUE_APP_API_ENDPOINT + "/api/v1/side-revenues",
      resource_filter: {},
      form_name: "DoanhThuNgoaiForm",
      modal_name: "modal-side-revenues-form",
      export_file_name: "doanh_thu_bosch_" + moment().format("DD_MM_YYYY"),
    }
  }
}
</script>
