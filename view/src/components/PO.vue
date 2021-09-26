<template>
  <div>
    <h2>Purchasing Order</h2>
    <!-- <span> -->
    <!-- <b-button variant="primary">Thêm</b-button><br></span> -->
    <div>
      <b-button
        @click="form_data = {}"
        v-b-modal.modal-po-form
        variant="primary"
        >Thêm Mới</b-button
      >
      &nbsp;
      <b-button
        @click="export_excel"
        variant="primary"
        >Export Excel</b-button
      >
      <hr style="border-color: rgba(0, 0, 0, 0.1); margin: 20px" />

      <b-modal
        id="modal-po-form"
        no-close-on-backdrop
        hide-header-close
        title="Thêm PO"
      >
        <po-form
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
          <th>Pn 13</th>
          <th>Pn 10</th>
          <th>Bosch_No</th>
          <th>Zexel_No</th>
          <th>Stamping</th>
          <th>Quốc Gia</th>
          <th>English Name</th>
          <th>Import Name<br />(Tên nhập khẩu)</th>
          <th>App Name <br />(Tên Ứng Dụng)</th>
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
          <th></th>
        </tr>
      </thead>
    </table>
  </div>
</template>
 
<script>
import "bootstrap/dist/css/bootstrap.min.css";
import "jquery/dist/jquery.min.js";
import $ from "jquery";

import "datatables.net-dt/js/dataTables.dataTables";
import "datatables.net-dt/css/jquery.dataTables.min.css";

import POForm from "./POForm.vue";
import axios from "axios";

let columns = [
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
  { data: "dap_price", render: $.fn.dataTable.render.number(",", ".", 2) },
  {
    data: "extension_price",
    render: $.fn.dataTable.render.number(",", ".", 2),
  },
  { data: "gia_von", render: $.fn.dataTable.render.number(",", ".", 2) },
  { data: "gia_si", render: $.fn.dataTable.render.number(",", ".", 2) },
  { data: "gia_le", render: $.fn.dataTable.render.number(",", ".", 2) },
  { data: "lead_time" },
  { data: "customer" },
  { data: "remarks" },
  {
    data: null,
    width: 100,
    defaultContent:
      '<button type="button" action="edit" v-b-modal.modal-po-form class="btn btn-warning flat">Sửa</button>\
      <button type="button" action="delete" class="btn btn-danger flat">Xóa</button>',
  },
];

export default {
  data: function () {
    return {
      table: null,
      form_data: {},
      action: "Tạo",
      sheets: [{ name: "SheetOne" }],
    };
  },
  components: {
    "po-form": POForm,
  },
  mounted() {
    let base_url = process.env.VUE_APP_API_ENDPOINT;
    let url = base_url + "/api/v1/purchasing-orders";
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
      scrollX: true
    });


    $("#poes_table tbody").on("click", "button", function () {
      var data = component.table.row($(this).parents("tr")).data();
      if ($(this).attr("action") == "delete") {
        component.delete_po(data.id);
        return;
      }

      component.$bvModal.show("modal-po-form");
      component.form_data = data;
      if ("id" in data) {
        component.action = "Sửa";
      } else {
        component.action = "Tạo";
      }
    });
  },
  methods: {
    export_excel(){
      let base_url = process.env.VUE_APP_API_ENDPOINT;
      let url = base_url + "/api/v1/tools/to-xlsx";
      let cell_raw_data = this.table.rows({filter:'applied'}).data()

      let table_header_text = []
      let table_header_name = []
      let table_data = []

      this.table.columns().every(function() {
        table_header_text.push( this.header().textContent )
      })

      for (let c=0; c < columns.length-1; c++){
        table_header_name.push(columns[c].data)
      }

      for (let d=0; d < cell_raw_data.length; d++){
        let row = []
        for (let c=0; c < table_header_name.length; c++){
          row.push(cell_raw_data[d][table_header_name[c]])
        }
        table_data.push(row)
      }
      console.log(table_data)
      console.log(table_header_text)
      table_data = [].concat([table_header_text], table_data)

      // Download file
      axios({
        url: url,
        method: 'post',
        data: table_data,
        responseType: 'blob', // important
      }).then((response) => {
        const url = window.URL.createObjectURL(new Blob([response.data]));
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download', 'po.xlsx');
        document.body.appendChild(link);
        link.click();
      });

    },
    refresh_table_data() {
      this.table.ajax.reload();
    },
    delete_po(id) {
      let base_url = process.env.VUE_APP_API_ENDPOINT;
      let url = base_url + "/api/v1/purchasing-orders" + "/" + id;
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

#poes_table button {
  display: inline-block;
  height: 100px;
}

table.dataTable td {
  padding: 3px 10px;
  width: 1px;
  white-space: nowrap;
}
</style>
