<template>
  <div>
    <h2>Xuất - Nhập - Tồn</h2>
    <!-- <span> -->
    <!-- <b-button variant="primary">Thêm</b-button><br></span> -->
    <div>
      &nbsp;
      <b-button @click="export_excel" variant="primary">Export Excel</b-button>

      <hr style="border-color: rgba(0, 0, 0, 0.1); margin: 20px" />
    </div>
    <table
      class="table table-hover table-bordered cell-border stripe"
      id="poes_table"
    >
      <thead>
        <tr>
          <!-- <th>No.</th> -->
          <th>Ứng Dụng</th>
          <th>Pn 13</th>
          <th>Bosch No</th>
          <th>Zexel No</th>
          <th>Stamping</th>
          <th>English Name</th>
          <th>Import Name<br />(Tên nhập khẩu)</th>
          <th>App Name <br />(Tên Ứng Dụng)</th>
          <th>Giá Nhập DAP <br />(USD)</th>
          <th>Số Lượng Nhập</th>
          <th>Số Lượng Xuất</th>
          <th>Tồn Cuối</th>
          <th>Total/PO</th>
          <th>Back Order</th>
          <th>Tiền BackOrder</th>
          <th>Giá Bán Sỉ</th>
          <th>Giá Bán Lẻ</th>
        </tr>
      </thead>
      <tfoot>
        <tr>
          <!-- <th>No.</th> -->
          <th>Ứng Dụng</th>
          <th>Pn 13</th>
          <th>Bosch No</th>
          <th>Zexel No</th>
          <th>Stamping</th>
          <th>English Name</th>
          <th>Import Name<br />(Tên nhập khẩu)</th>
          <th>App Name <br />(Tên Ứng Dụng)</th>
          <th>Giá Nhập DAP <br />(USD)</th>
          <th>Số Lượng Nhập</th>
          <th>Số Lượng Xuất</th>
          <th>Tồn Cuối</th>
          <th>Total/PO</th>
          <th>Back Order</th>
          <th>Tiền BackOrder</th>
          <th>Giá Bán Sỉ</th>
          <th>Giá Bán Lẻ</th>
        </tr>
      </tfoot>
    </table>
  </div>
</template>
 
<script>
import $ from "jquery";

import tool_mixin from "./tool_mixins.js";

export default {
  mixins: [tool_mixin],
  data: function () {
    return {
      table: null,
      export_file_name: "xuat_nhap_ton",
      columns: [
        { data: "ung_dung" },
        { data: "pn_13" },
        { data: "bosch_no" },
        { data: "xecel_no" },
        { data: "stamping" },
        { data: "english_des" },
        { data: "import_des" },
        { data: "app_des" },
        {
          data: "dap_price",
          render: $.fn.dataTable.render.number(",", ".", 2),
        },
        { data: "so_luong_nhap" },
        { data: "so_luong_xuat" },
        { data: "ton_cuoi" },
        { data: "total_po" },
        { data: "bor" },
        {
          data: "bor_price",
          render: $.fn.dataTable.render.number(",", ".", 2),
        },
        { data: "gia_si", render: $.fn.dataTable.render.number(",", ".", 2) },
        { data: "gia_le", render: $.fn.dataTable.render.number(",", ".", 2) },
      ],
    };
  },
  mounted() {
    let base_url = process.env.VUE_APP_API_ENDPOINT;
    let url = base_url + "/api/v1/xuat-nhap-ton";

    this.table = $("#poes_table").DataTable({
      ajax: {
        url: url,
        dataSrc: "",
      },
      columnDefs: [
        {
          defaultContent: "-",
          targets: "_all",
        },
      ],
      columns: this.columns,
      scrollX: true,
      autoWidth: true,
      responsive: true,
      initComplete: function () {
        // Apply the search
        this.api()
          .columns()
          .every(function () {
            var that = this;

            $("input", this.footer()).on("keyup change clear", function () {
              if (that.search() !== this.value) {
                that.search(this.value).draw();
              }
            });
          });
      },
    });

    $("#poes_table tfoot th").each(function () {
      var title = $(this).text();
      $(this).html('<input type="text" placeholder="Tìm ' + title + '" />');
    });
  },
};
</script>

<style scoped>
table.dataTable thead th {
  white-space: nowrap;
}
</style>