<template>
  <div>
    <h2>Nhập Kho</h2>
    <!-- <span> -->
    <!-- <b-button variant="primary">Thêm</b-button><br></span> -->
    <div>
      <b-button
        @click="form_data = {}"
        v-b-modal.modal-nhap-kho-form
        variant="primary"
        >Thêm Mới</b-button
      >
      <hr style="border-color: rgba(0, 0, 0, 0.1); margin: 20px" />

      <b-modal
        id="modal-nhap-kho-form"
        no-close-on-esc
        no-close-on-backdrop
        hide-header-close
        title="Nhập Kho"
      >
        <NhapKhoForm
          @refresh_table_data="refresh_table_data"
          :form_data="form_data"
          :action="action"
        />
        <template #modal-footer>
          <br />
        </template>
      </b-modal>
    </div>
    <table
      class="table table-hover table-bordered cell-border stripe"
      id="poes_table"
    >
      <thead>
        <tr>
          <th>PO. No</th>
          <th>Ngày Nhập</th>
          <th>Số Chứng Từ</th>
          <th>Cty Cung Cấp</th>
          <th>Pn 13</th>
          <th>Pn 10</th>
          <th>Bosch_No</th>
          <th>Zexel_No</th>
          <th>Stamping</th>
          <th>English Name</th>
          <th>Import Name<br />(Tên Nhập Khẩu)</th>
          <th>App Name<br />(Tên Ứng Dụng)</th>
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
          <th></th>
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
import NhapKhoForm from "./NhapKhoForm.vue";

let columns = [
  { data: "po_no" },
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
  { data: "dap_price", render: $.fn.dataTable.render.number(",", ".", 2) },
  {
    data: "extension_price",
    render: $.fn.dataTable.render.number(",", ".", 2),
  },
  { data: "tax" },
  { data: "gia_von", render: $.fn.dataTable.render.number(",", ".", 2) },
  { data: "gia_si", render: $.fn.dataTable.render.number(",", ".", 2) },
  { data: "gia_le", render: $.fn.dataTable.render.number(",", ".", 2) },
  { data: "gia_goc", render: $.fn.dataTable.render.number(",", ".", 2) },
  { data: "tong_gia_goc", render: $.fn.dataTable.render.number(",", ".", 2) },
  { data: "ratio" },
  { data: "vat_percentage" },
  {
    data: null,
    width: 100,
    defaultContent:
      '<button type="button" action="edit" class="btn btn-warning flat">Sửa</button>\
    <button type="button" action="delete" class="btn btn-danger flat">Xóa</button>',
  },
];

export default {
  data: function () {
    return {
      table: null,
      form_data: {
        provider: "Bosch",
        bosch_no: "",
        z_exel_no: "",
        english_des: "",
      },
      action: "Tạo",
    };
  },
  components: {
    NhapKhoForm,
  },
  mounted() {
    let base_url = "http://localhost:8000";
    let url = base_url + "/api/v1/nhap-kho";
    var component = this;
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
      columns: columns,
      scrollX: true,
      autoWidth: true,
    });

    $("#poes_table tbody").on("click", "button", function () {
      var data = component.table.row($(this).parents("tr")).data();
      if ($(this).attr("action") == "delete") {
        component.delete_po(data.id);
        return;
      }

      component.$bvModal.show("modal-nhap-kho-form");
      component.form_data = data;
      if ("id" in data) {
        component.action = "Sửa";
      } else {
        component.action = "Tạo";
      }
    });
  },
  methods: {
    refresh_table_data() {
      this.table.ajax.reload();
    },
    delete_po(id) {
      let base_url = "http://localhost:8000";
      let url = base_url + "/api/v1/nhap-kho" + "/" + id;
      axios.delete(url).then(() => {
        this.$root.$bvModal.msgBoxOk(`Đã Xóa`);
        this.refresh_table_data();
      });
    },
  },
};
</script>

<style scoped>
table.dataTable thead th {
  white-space: nowrap;
}
</style>