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

import DataTable from "./BaseTable.vue"
import moment from "moment";
// import $ from "jquery";

export default {
  components: {
    DataTable,
  },
    data: function () {
    return {
      title: "Danh Sách Khách Hàng",
      column_names: ["Mã Khách Hàng", "Tên Khách hàng", ""],
      column_definitions: [
        { data: "code" },
        { data: "name" },
        {
          data: null,
          width: 100,
          defaultContent:
            '<button type="button"  action="edit"  class="btn btn-warning flat ">Sửa</button>\
            <button type="button"  action="delete" class="btn btn-danger flat ">Xóa</button>',
        },
      ],
      total_data: [
      ],
      resource_url: process.env.VUE_APP_API_ENDPOINT + "/api/v1/customers",
      resource_filter: {},
      form_name: "CustomerForm",
      modal_name: "modal-customer-form",
      export_file_name: "danh_sach_khach_hang_" + moment().format("DD_MM_YYYY"),
    }
  }
}
</script>
