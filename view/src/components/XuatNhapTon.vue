<template>
  <div>
    <h2>Xuất - Nhập - Tồn</h2>
    <!-- <span> -->
    <!-- <b-button variant="primary">Thêm</b-button><br></span> -->
    <div>
      <hr style="border-color: rgba(0, 0, 0, 0.1); margin: 20px" />
    </div>
    <table
      class="table table-hover table-bordered cell-border stripe"
      id="poes_table"
    >
      <thead>
        <tr>
          <th>No.</th>
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
    </table>
  </div>
</template>
 
<script>
// import "bootstrap/dist/css/bootstrap.min.css";
// import "jquery/dist/jquery.min.js";

// import "datatables.net-dt/js/dataTables.dataTables";
// import "datatables.net-dt/css/jquery.dataTables.min.css";
import $ from "jquery";

import axios from "axios";

let columns = [
  { data: "id" },
  { data: "ung_dung" },
  { data: "pn_13" },
  { data: "bosch_no" },
  { data: "xecel_no" },
  { data: "stamping" },
  { data: "english_des" },
  { data: "import_des" },
  { data: "app_des" },
  { data: "dap_price", render: $.fn.dataTable.render.number(",", ".", 2) },
  { data: "so_luong_nhap" },
  { data: "so_luong_xuat" },
  { data: "ton_cuoi" },
  { data: "total_po" },
  { data: "bor" },
  { data: "bor_price", render: $.fn.dataTable.render.number(",", ".", 2) },
  { data: "gia_si", render: $.fn.dataTable.render.number(",", ".", 2) },
  { data: "gia_le", render: $.fn.dataTable.render.number(",", ".", 2) },
];

export default {
  mounted() {
    axios.get("http://localhost:8000/api/v1/xuat-nhap-ton").then((response) => {
      $("#poes_table").DataTable({
        data: response.data,
        columnDefs: [
          {
            defaultContent: "-",
            targets: "_all",
          },
        ],
        columns: columns,
        scrollX: true,
        autoWidth: true,
        responsive: true,
      });
    });
  },
};
</script>

<style scoped>
table.dataTable thead th {
  white-space: nowrap;
}
</style>