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
  :show_table_footer_from_parent=show_table_footer
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
      title: "Kết Quả Kinh Doanh",
      column_names: ["Số thứ tự", "Nội Dung", "Giá Trị", ""],
      column_definitions: [
        { data: "no" },
        { data: "content" },
        { data: "value",  render: $.fn.dataTable.render.number(",", ".", 2) },
        {}
      ],
      total_data: [
      ],
      resource_url: process.env.VUE_APP_API_ENDPOINT + "/api/v1/business-results",
      resource_filter: {},
      form_name: "",
      modal_name: "",
      export_file_name: "ket_qua_kinh_doanh_" + moment().format("DD_MM_YYYY"),
      show_table_footer: "true"
    }
  }
}
</script>
