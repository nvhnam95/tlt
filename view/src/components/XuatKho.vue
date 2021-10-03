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
      <b-button @click="export_excel" variant="primary">Export Excel</b-button>
      <hr style="border-color: rgba(0, 0, 0, 0.1); margin: 20px" />
      <p>Chọn ngày (ngày nhập):</p>
      <input id="date-filter" /><br /><br />
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
// import "bootstrap/dist/css/bootstrap.min.css";
// import "jquery/dist/jquery.min.js";

// import "datatables.net-dt/js/dataTables.dataTables";
// import "datatables.net-dt/css/jquery.dataTables.min.css";
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
        { data: "input_date" },
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
            '<button type="button" action="edit"  class="btn btn-warning flat">Sửa</button>\
            <button type="button" action="delete" class="btn btn-danger flat">Xóa</button>',
        },
      ],
      table_data_url: process.env.VUE_APP_API_ENDPOINT + "/api/v1/xuat-kho"
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
        this.api()
          .columns()
          .every(function () {
            var that = this;
            $("input", this.footer()).on("keyup change clear", function () {
              if (that.search() !== this.value) {
                if (this.value === "") {
                  that.search("").draw();
                } else {
                  that.search("^" + this.value + "$", true, false).draw();
                }
              }
            });
          });
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
    generate_search_boxes(){
      $('#poes_table tfoot th').each( function () {
        var title = $(this).text();
        $(this).html( '<input type="text" placeholder="Tìm '+title+'" />' );
      });

      // Date range
      var start = moment().subtract(29, "days");
      var end = moment();
      $("#date-filter").daterangepicker(
        {
          startDate: start,
          endDate: end,
          ranges: {
            "Cả Năm": [moment().startOf("year"), moment().endOf("year")],
            "Hôm nay": [moment(), moment()],
            "Hôm qua": [
              moment().subtract(1, "days"),
              moment().subtract(1, "days"),
            ],
            "7 ngày trước": [moment().subtract(6, "days"), moment()],
            "30 ngày trước": [moment().subtract(29, "days"), moment()],
            "Tháng Này": [moment().startOf("month"), moment().endOf("month")],
            "Tháng Trước": [
              moment().subtract(1, "month").startOf("month"),
              moment().subtract(1, "month").endOf("month"),
            ],
          },
           locale: {
            "format": "DD/MM/YYYY",
            "separator": " - ",
            "applyLabel": "OK",
            "cancelLabel": "Hủy",
            "fromLabel": "Từ",
            "toLabel": "Đến",
            "customRangeLabel": "Chọn khoảng thời gian",
            "weekLabel": "W",
            "daysOfWeek": [
                "CN",
                "T2",
                "T3",
                "T4",
                "T5",
                "T5",
                "T7"
            ],
            "monthNames": [
                "Tháng 1",
                "Tháng 2",
                "Tháng 3",
                "Tháng 4",
                "Tháng 5",
                "Tháng 6",
                "Tháng 7",
                "Tháng 8",
                "Tháng 9",
                "Tháng 10",
                "Tháng 11",
                "Tháng 12"
            ],
            "firstDay": 1
        },
        },
        this.date_range_filter_callback
      );
      this.date_range_filter_callback(start, end);
    },
    date_range_filter_callback(start, end) {
      let component = this;
      $("#reportrange span").html(
        start.format("MMMM D, YYYY") + " - " + end.format("MMMM D, YYYY")
      );
      component.refresh_table_data(start, end)
    },
    refresh_table_data(start=null, end=null) {
      if (this.table){
        if (start && end) {
          this.table.ajax.url(this.table_data_url + "?start=" + start.format('YYYY-MM-DD') + "&end=" + end.format('YYYY-MM-DD'))
        }
        this.table.ajax.reload();
      }
    },
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