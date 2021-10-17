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
      <table>
        <tr>
          <th class="">Tổng tiền Back Order:</th>
        </tr>
        <tr>
          <td class=" " id="tong_tien_back_order">{{tong_tien_back_order}} USD</td>
        </tr>
      </table> <br>

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
      tong_tien_back_order: 0,
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
        table_data_url: process.env.VUE_APP_API_ENDPOINT + "/api/v1/xuat-nhap-ton",
        date_filter_start: null,
        date_filter_end: null,
    }
  },
  mounted() {
    let url = this.table_data_url
    this.generate_search_boxes()
    let component = this
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
      language : {
        "lengthMenu": "Hiển thị _MENU_ dòng"
      },
      drawCallback: function () {
        var api = this.api();
        component.tong_tien_back_order = api.column( 14, {page:'all', search: 'applied'} ).data().sum().toLocaleString()
      },
    });
  }
};
</script>

<style scoped>
table.dataTable thead th {
  white-space: nowrap;
}
</style>