<template>
  <div>
    <h2>Xuất Kho</h2>
    <!-- <span> -->
    <!-- <b-button variant="primary">Thêm</b-button><br></span> -->
    <div>
      <b-button v-b-modal.modal-po-form variant="primary">Thêm Mới</b-button>
      <hr style="border-color: rgba(0, 0, 0, 0.1); margin: 20px;"> 

      <b-modal id="modal-po-form" no-close-on-esc no-close-on-backdrop hide-header-close title="Xuất Kho">
        <XuatKhoForm />
        <template #modal-footer>
          <br>
        </template>
      </b-modal>
    </div>
    <table
      class="table table-hover table-bordered cell-border stripe"
      id="poes_table"
    >
      <thead>
        <tr>
          <th>No.</th>
          <th>Ngày Nhập</th>
          <th>Pn 13</th>
          <th>Số Lượng</th>
          <th>Giá Gốc<br />(VND)</th>
          <th>Tiền Gốc<br />(VND)</th>
          <th>English Name</th>
          <th>Import Name<br/>(Tên Nhập Khẩu)</th>
          <th>App Name<br>(Tên Ứng Dụng)</th>
          <th>Khách Hàng</th>
        </tr>
      </thead>
    </table>
  </div>
</template>
 
<script>
import "bootstrap/dist/css/bootstrap.min.css";
import "jquery/dist/jquery.min.js";

import "datatables.net-dt/js/dataTables.dataTables";
import "datatables.net-dt/css/jquery.dataTables.min.css";
import $ from "jquery";

import axios from "axios";
import XuatKhoForm from "./XuatKhoForm.vue"

let columns = [
  { data: "id" },
  { data: "input_date" },
  { data: "pn_13" },
  { data: "quantity" },
  { data: "gia_goc" },
  { data: "tien_goc" },
  { data: "english_des" },
  { data: "import_des" },
  { data: "app_des" },
  { data: "customer" },
];

export default {
  components: {
      XuatKhoForm,
    },
  mounted() {
    axios
      .get("http://localhost:8000/api/v1/xuat-kho")
      .then((response) => {
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
  }
};
</script>

<style scoped>
table.dataTable thead th {
  white-space: nowrap;
}
</style>