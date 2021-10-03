<template>
  <div>
    <h2>Xuất - Nhập - Tồn</h2>
    <!-- <span> -->
    <!-- <b-button variant="primary">Thêm</b-button><br></span> -->
    <div>
      &nbsp;
      <b-button
        @click="export_excel"
        variant="primary"
        >Export Excel</b-button
      >
      <div id="start-date"></div>
      <hr style="border-color: rgba(0, 0, 0, 0.1); margin: 20px" />
      <p>Chọn ngày (ngày cập nhật):</p>
      <input id="date-filter" /><br /><br />
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

import tool_mixin from "./tool_mixins.js" ;
import moment from "moment";
import "daterangepicker/daterangepicker";
import "daterangepicker/daterangepicker.css";


export default {
  mixins: [tool_mixin],
  data: function (){
    return {
      table: null,
      export_file_name: 'xuat_nhap_ton_' + moment().format('DD_MM_YYYY'),
      columns: [
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
      ],
        options: [
          { value: null, text: 'toàn thời gian' },
          { value: 'a', text: 'tuần trước' },
          { value: 'b', text: 'tháng trước' },
          { value: { C: '3PO' }, text: 'Lựa chọn' },
          { value: 'd', text: 'This one is disabled', disabled: true }
        ],
        table_data_url: process.env.VUE_APP_API_ENDPOINT + "/api/v1/xuat-nhap-ton"
    }
  },
  mounted() {
    let url = this.table_data_url
    this.generate_search_boxes()
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
          this.api().columns().every( function () {
              var that = this;
              $('input', this.footer()).on('keyup change clear', function () {
                if (that.search() !== this.value) {
                  if (this.value === ''){
                      that.search("").draw();
                  }
                  else {
                    that.search("^" + this.value + "$" , true, false).draw();
                  }
                }
              });
          });
          // Add time range filter
      },
      language : {
        "lengthMenu": "Hiển thị _MENU_ dòng"
      }
    });
  },
  methods: {
    generate_search_boxes() {
      $("#poes_table tfoot th").each(function () {
        var title = $(this).text();
        $(this).html('<input type="text" placeholder="Tìm ' + title + '" />');
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
    }
  }
};
</script>

<style scoped>
table.dataTable thead th {
  white-space: nowrap;
}
</style>