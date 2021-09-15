<template>
  <div>
    <h2>Purchasing Order</h2>
    <!-- <span> -->
    <!-- <b-button variant="primary">Thêm</b-button><br></span> -->
    <div>
      <b-button v-b-modal.modal-po-form variant="primary">Thêm Mới</b-button>
      <hr style="border-color: rgba(0, 0, 0, 0.1); margin: 20px;"> 

      <b-modal id="modal-po-form" no-close-on-esc no-close-on-backdrop hide-header-close title="Thêm PO">
        <POForm />
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
          <th>Pn 13</th>
          <th>Pn 10</th>
          <th>Bosch_No</th>
          <th>Zexel_No</th>
          <th>Stamping</th>
          <th>Quốc Gia</th>
          <th>English Name</th>
          <th>Import Name<br />(Tên nhập khẩu)</th>
          <th>App Name <br>(Tên Ứng Dụng)</th>
          <th>Thuế VAT+TNK</th>
          <th>Quantity</th>
          <th>Giá Nhập DAP <br />(USD)</th>
          <th>Extension Price <br />(USD)</th>
          <th>Giá Vốn<br />Khởi Điểm</th>
          <th>Giá Bán Sỉ <br />(VND)</th>
          <th>Giá Bán Lẻ <br />(VND)</th>
          <th>Lead Time</th>
          <th>Customer</th>
          <th>Remarks</th>
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
import POForm from "./POForm.vue"

let columns = [
  { data: "id" },
  { data: "po_no", width: 150 },
  { data: "pn_13" },
  { data: "pn_10" },
  { data: "bosch_no" },
  { data: "z_exel_no" },
  { data: "stamping" },
  { data: "country" },
  { data: "english_des" },
  { data: "import_des" },
  { data: "app_des" },
  { data: "tax" },
  { data: "quantity" },
  { data: "dap_price" },
  { data: "extension_price" },
  { data: "gia_von" },
  { data: "gia_si" },
  { data: "gia_le" },
  { data: "lead_time" },
  { data: "customer" },
  { data: "remarks" },
];

export default {
  components: {
      POForm,
    },
  mounted() {
    axios
      .get("http://localhost:8000/api/v1/purchasing-orders")
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
          // fixedHeader: true,
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