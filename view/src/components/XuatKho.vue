<template>
  <div>
    <h2>Xuất Kho</h2>
    <!-- <span> -->
    <!-- <b-button variant="primary">Thêm</b-button><br></span> -->
    <div>
      <b-button
        @click="form_data = {}"
        v-b-modal.modal-xuat-kho-form
        variant="primary"
        >Thêm Mới</b-button
      >
      &nbsp;
      <b-button @click="export_excel([['Tổng tiền gốc: ', tong_tien_goc + ' đ']])" variant="primary">Export Excel</b-button>
      <hr style="border-color: rgba(0, 0, 0, 0.1); margin: 20px" />

      <table>
        <tr>
          <th>Từ Ngày</th>
          <th>Đến ngày</th>
          <th></th>
          <th class="px-5">Tổng tiền gốc </th>
        </tr>
        <tr>
          <td><input id="date-filter-start" /></td>
          <td><input id="date-filter-end" /></td>
          <td></td>
          <td class="px-5" id="tong_tien_goc">{{tong_tien_goc}} đồng</td>
        </tr>
      </table> <br>
      <b-modal
        id="modal-xuat-kho-form"
        no-close-on-backdrop
        hide-header-close
        title="Xuất Kho"
      >
        <XuatKhoForm
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
          <th>Ngày Nhập</th>
          <th>Pn 13</th>
          <th>Số Lượng</th>
          <th>Giá Gốc<br />(VND)</th>
          <th>Tiền Gốc<br />(VND)</th>
          <th>Giá bán sỉ<br />(VND)</th>
          <th>Giá bán lẻ<br />(VND)</th>
          <th>English Name</th>
          <th>Import Name<br />(Tên Nhập Khẩu)</th>
          <th>App Name<br />(Tên Ứng Dụng)</th>
          <th>Khách Hàng</th>
          <th></th>
        </tr>
      </thead>
        <tfoot>
            <tr>
          <th>Ngày Nhập</th>
          <th>Pn 13</th>
          <th>Số Lượng</th>
          <th>Giá Gốc<br />(VND)</th>
          <th>Tiền Gốc<br />(VND)</th>
          <th>Giá bán sỉ<br />(VND)</th>
          <th>Giá bán lẻ<br />(VND)</th>
          <th>English Name</th>
          <th>Import Name<br />(Tên Nhập Khẩu)</th>
          <th>App Name<br />(Tên Ứng Dụng)</th>
          <th>Khách Hàng</th>
          <th></th>
            </tr>
        </tfoot>
    </table>
  </div>
</template>
 
<script>
import $ from "jquery";

import axios from "axios";
import XuatKhoForm from "./XuatKhoForm.vue";
import tool_mixin from "./tool_mixins.js";
import moment from "moment";
import "daterangepicker/daterangepicker";
import "daterangepicker/daterangepicker.css";

export default {
  mixins: [tool_mixin],
  data: function () {
    return {
      tong_tien_goc: 0,
      table: null,
      export_file_name: "xuat_kho_" + moment().format("DD_MM_YYYY"),
      form_data: {
        provider: "Bosch",
        gia_goc: "",
        gia_si: "",
        gia_le: "",
        tien_goc: "",
      },
      action: "Tạo",
      columns: [
        { data: "input_date",
          render: function(data){return moment(data).format("DD/MM/YYYY");}
        },
        { data: "pn_13" },
        { data: "quantity" },
        { data: "gia_goc", render: $.fn.dataTable.render.number(",", ".", 2) },
        { data: "tien_goc", render: $.fn.dataTable.render.number(",", ".", 2) },
        { data: "gia_si", render: $.fn.dataTable.render.number(",", ".", 2) },
        { data: "gia_le", render: $.fn.dataTable.render.number(",", ".", 2) },
        { data: "english_des" },
        { data: "import_des" },
        { data: "app_des" },
        { data: "customer" },
        {
          data: null,
          width: 100,
          defaultContent:
            '<button type="button"  action="edit"  class="btn btn-warning flat ">Sửa</button>\
            <button type="button"  action="delete" class="btn btn-danger flat ">Xóa</button>',
        },
      ],
      table_data_url: process.env.VUE_APP_API_ENDPOINT + "/api/v1/xuat-kho",
      date_filter_start: null,
      date_filter_end: null,
    };
  },
  components: {
    XuatKhoForm,
  },
  mounted() {
    let url = this.table_data_url
    this.generate_search_boxes()
    var component = this;
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
        },
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
        component.tong_tien_goc = api.columns( 4, {page:'all', search: 'applied'} ).data().sum().toLocaleString()
      },
      language: {
        lengthMenu: "Hiển thị _MENU_ dòng",
      },
    });

    $('#poes_table tfoot th').each( function () {
      var title = $(this).text();
      $(this).html( '<input type="text" placeholder="Tìm '+title+'" />' );
    });

    $("#poes_table tbody").on("click", "button", function () {
      var data = component.table.row($(this).parents("tr")).data();
      if ($(this).attr("action") == "delete") {
        component.delete_po(data.id);
        return;
      }

      component.$bvModal.show("modal-xuat-kho-form");
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
      let url = base_url + "/api/v1/xuat-kho" + "/" + id;
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