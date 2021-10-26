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
      &nbsp;
      <b-button @click="export_excel([['Tổng extension price: ', tong_extension_price + ' USD']])" variant="primary">Export Excel</b-button>
      <hr style="border-color: rgba(0, 0, 0, 0.1); margin: 20px" />

      <table>
        <tr>
          <th>Từ Ngày</th>
          <th>Đến ngày</th>
          <th></th>
          <th class="px-5">Tổng Extension Price</th>
        </tr>
        <tr>
          <td><input id="date-filter-start" /></td>
          <td><input id="date-filter-end" /></td>
          <td></td>
          <td class="px-5 " id="tong_extension_price">{{tong_extension_price}} USD</td>
        </tr>
      </table> <br>

      <b-modal
        id="modal-nhap-kho-form"
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
      <tfoot>
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
      </tfoot>
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
import tool_mixin from "./tool_mixins.js";
import moment from "moment";
import "daterangepicker/daterangepicker";
import "daterangepicker/daterangepicker.css";

export default {
  mixins: [tool_mixin],
  data: function () {
    return {
      tong_extension_price: 0,
      table: null,
      export_file_name: "nhap_kho_" + moment().format("DD_MM_YYYY"),
      form_data: {
        provider: "Bosch",
        bosch_no: "",
        z_exel_no: "",
        english_des: "",
      },
      action: "Tạo",
      columns: [
        { data: "po_no" },
        { data: "input_date", 
          render: function(data){return moment(data).format("DD/MM/YYYY");}
        },
        { data: "license_no" },
        { data: "provider" },
        { data: "pn_13" },
        { data: "pn_10" },
        { data: "bosch_no" },
        { data: "z_exel_no" },
        { data: "stamping" },
        { data: "english_des" },
        { data: "import_des"},
        { data: "app_des" },
        { data: "quantity" },
        {
          data: "dap_price",
          render: $.fn.dataTable.render.number(",", ".", 2),
        },
        {
          data: "extension_price",
          render: $.fn.dataTable.render.number(",", ".", 2),
        },
        { data: "tax" },
        { data: "gia_von", render: $.fn.dataTable.render.number(",", ".", 2) },
        { data: "gia_si", render: $.fn.dataTable.render.number(",", ".", 2) },
        { data: "gia_le", render: $.fn.dataTable.render.number(",", ".", 2) },
        { data: "gia_goc", render: $.fn.dataTable.render.number(",", ".", 2) },
        {
          data: "tong_gia_goc",
          render: $.fn.dataTable.render.number(",", ".", 2),
        },
        { data: "ratio" },
        { data: "vat_percentage" },
        {
          data: null,
          width: 100,
          defaultContent:
            '<button type="button" action="edit" class="btn btn-warning flat">Sửa</button>\
          <button type="button" action="delete" class="btn btn-danger flat">Xóa</button>',
        },
      ],
      table_data_url: process.env.VUE_APP_API_ENDPOINT + "/api/v1/nhap-kho",
      date_filter_start: null,
      date_filter_end: null,
    };
  },
  components: {
    NhapKhoForm,
  },
  mounted() {
    let url = this.table_data_url
    var component = this;
    component.generate_search_boxes();
    this.table = $("#poes_table").DataTable({
      pageLength: 50,
      ajax: {
        url: url,
        dataSrc: "",
      },
      columnDefs: [
        {
          defaultContent: "-",
          targets: "_all",
          
        }
      ],
      columns: this.columns,
      scrollX: true,
      autoWidth: true,
      initComplete: function () {
          // Apply the search
          this.api().columns().every( function () {
              var that = this;
              let column_data_src = this.dataSrc()
              let allow_partial_search = ["pn_13", "english_des", "import_des", "app_des"]
              $('input', this.footer()).on('keyup change clear', function () {
                if (that.search() !== this.value) {
                  if (this.value === ''){
                      that.search("").draw();
                  }
                  else {
                    if (allow_partial_search.includes(column_data_src)){
                        that.search(this.value).draw();
                    }
                    else {
                      that.search("^" + this.value + "$" , true, false).draw();
                    }
                    
                  }
                }
              });
          });
      },
      drawCallback: function () {
        var api = this.api();
        component.tong_extension_price = api.column( 14, {page:'all', search: 'applied'} ).data().sum().toLocaleString()
      },
      language: {
        lengthMenu: "Hiển thị _MENU_ dòng",
      },
    });

    // Handle button: Edit, Remove
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
    delete_po(id) {
      let base_url = process.env.VUE_APP_API_ENDPOINT;
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
button {
  padding: 5px;
}
th, td {
    white-space: nowrap;
}
table.dataTable tbody th, table.dataTable tbody td {
    padding: 0px 10px; /* e.g. change 8x to 4px here */
}

</style>
