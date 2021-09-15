<template>
  <div>
    <h2>Nhập Kho</h2>
    <!-- <span> -->
    <!-- <b-button variant="primary">Thêm</b-button><br></span> -->
    <div>
      <b-button v-b-modal.modal-po-form variant="primary">Thêm Mới</b-button>
      <hr style="border-color: rgba(0, 0, 0, 0.1); margin: 20px;"> 

      <b-modal id="modal-po-form" no-close-on-esc no-close-on-backdrop hide-header-close title="Nhập Kho">
        <NhapKhoForm />
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
          <th>PO. No</th>
          <th>Ngày Nhập</th>
          <th>Số Chứng Từ</th>
          <th>Công Ty Cung Cấp</th>
          <th>Pn 13</th>
          <th>Pn 10</th>
          <th>Bosch_No</th>
          <th>Zexel_No</th>
          <th>Stamping</th>
          <th>English Name</th>
          <th>Import Name<br/>(Tên Nhập Khẩu)</th>
          <th>App Name<br>(Tên Ứng Dụng)</th>
          <th>Số Lượng</th>
          <th>Giá Nhập DAP <br />(USD)</th>
          <th>Extension Price<br />(USD)</th>
          <th>Thuế NK+VAT</th>
          <th>Giá Vốn</th>
          <th>Giá Bán Sỉ<br />(VND)</th>
          <th>Giá Bán Lẻ <br />(VND)</th>
          <th>Giá Gốc</th>
          <th>Tổng Giá Gốc</th>
          <th>Tỷ Giá</th>
          <th>% Thuế VAT</th>

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
import NhapKhoForm from "./NhapKhoForm.vue"

let columns = [
  { data: "id" },
  { data: "po_no", width: 150 },
  { data: "input_date" },
  { data: "license_no" },
  { data: "provider" },
  { data: "pn_13" },
  { data: "pn_10" },
  { data: "bosch_no" },
  { data: "z_exel_no" },
  { data: "stamping" },
  { data: "english_des" },
  { data: "import_des" },
  { data: "app_des" },
  { data: "quantity" },
  { data: "dap_price" },
  { data: "extension_price" },
  { data: "tax" },
  { data: "gia_von" },
  { data: "gia_si" },
  { data: "gia_le" },
  { data: "gia_goc" },
  { data: "tong_gia_goc" },
  { data: "ratio" },
  { data: "vat_percentage" },
];

export default {
  components: {
      NhapKhoForm,
    },
  mounted() {
    axios
      .get("http://localhost:8000/api/v1/nhap-kho")
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