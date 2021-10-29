<template>
  <div>
    <div class="w-25 p-3">
      <h3>Khách Hàng</h3>
      <table>
        <tr>
          <td>
            <b-form-select
              class="form-select"
              v-model="selected_khach_hang_name"
              :options="danh_sach_khach_hang"
              value-field="name"
              text-field="name"
              v-on:input="render_cong_no"
            >
              <template #first>
                <b-form-select-option :value="null" disabled
                  >-- Chọn Khách Hàng --</b-form-select-option
                >
              </template>
            </b-form-select>
          </td>

          <td>
            <div class="">&nbsp;&nbsp;&nbsp;&nbsp;</div>
          </td>

          <td>
            <b-button
              @click="form_data = {}"
              v-b-modal.modal-cong-no-khach-hang-form
              variant="primary"
              >Thêm Mới</b-button
            >
          </td>
          <td>
            <b-button
              @click="export_cong_no_excel()"
              v-if="this.selected_khach_hang_id"
              variant="primary"
              >Export Excel</b-button
            >
          </td>
        </tr>
      </table>
      <b-modal
        id="modal-cong-no-khach-hang-form"
        no-close-on-backdrop
        hide-header-close
        title=""
      >
        <CongNoKhachHangForm
          @refresh_table_data="refresh_table_data"
          @render_cong_no="render_cong_no"
          :form_data="form_data"
          :action="action"
          :resource_url_from_parent="resource_url"
          :modal_name_from_parent="modal_name"
        />

        <template #modal-footer>
          <br />
        </template>
      </b-modal>
    </div>
    <table v-show="this.selected_khach_hang_id">
      <tbody>
        <td>
          <table
            class="table table-hover table-bordered cell-border stripe"
            id="table"
          >
            <thead>
              <tr>
                <th>Tên</th>
                <th>Công Ty</th>
                <th>Địa Chỉ</th>
                <th>Mã Số Thuế</th>
                <th>Ghi Chú</th>
                <th></th>
              </tr>
            </thead>
          </table>
        </td>
        <td>
          <table
            class="table table-hover table-bordered cell-border stripe"
            id="table_summary"
          >
            <thead>
              <tr>
                <th>Tổng Nợ</th>
                <th>Đã Thanh Toán</th>
                <th>Còn Lại</th>
              </tr>
            </thead>
            <tbody>
              <tr class="optimize_height">
                <td>{{ tong_no.toLocaleString() }}</td>
                <td>{{ da_thanh_toan.toLocaleString() }}</td>
                <td>{{ con_lai.toLocaleString() }}</td>
              </tr>
            </tbody>
          </table>
        </td>
      </tbody>
    </table>
    <div v-if="this.selected_khach_hang_id">
      <hr style="border-color: rgba(0, 0, 0, 0.1); margin: 20px" />
      <b-tabs>
        <b-tab title="Khoản Nợ">
          <div>
            <KhoanNoTable
              active
              @update_tong_no="update_tong_no"
              :khach_hang_id_from_parent="selected_khach_hang_id"
              :title="''"
              :column_names="khoan_no_column_names"
              :columns="khoan_no_column_definitions"
              :total_data_from_parent="[]"
              :resource_url_from_parent="khoan_no_resource_url"
              :form_name_from_parent="'form_name'"
              :modal_name_from_parent="'modal_name'"
              :resource_filter_from_parent="resource_filter"
              :export_file_name_from_parent="'cac_khoan_no_'"
              :table_id_from_parent="'khoan_no_table'"
              :hide_table_footer_from_parent="hide_table_footer"
            />
          </div>
        </b-tab>
        <b-tab title="Thanh Toán">
          <div>
            <ThanhToanTable
              @update_da_thanh_toan="update_da_thanh_toan"
              :khach_hang_id_from_parent="selected_khach_hang_id"
              :title="''"
              :column_names="thanh_toan_column_names"
              :columns="thanh_toan_column_definitions"
              :total_data_from_parent="[]"
              :resource_url_from_parent="thanh_toan_resource_url"
              :form_name_from_parent="'form_name'"
              :modal_name_from_parent="'modal_name'"
              :resource_filter_from_parent="resource_filter"
              :export_file_name_from_parent="'cac_thanh_toan_'"
              :table_id_from_parent="'thanh_toan_table'"
              :hide_table_footer_from_parent="hide_table_footer"
            /></div
        ></b-tab>
      </b-tabs>
    </div>
  </div>
</template>

<script>
import $ from "jquery";
import axios from "axios";
import tool_mixin from "../tool_mixins.js";
import ThanhToanTable from "./ThanhToan.vue";
import KhoanNoTable from "./KhoanNo.vue";
import CongNoKhachHangForm from "./CongNoKhachHangForm.vue";
import moment from "moment";
import "datatables.net-dt/js/dataTables.dataTables";
import "datatables.net-dt/css/jquery.dataTables.min.css";

export default {
  mixins: [tool_mixin],
  components: { ThanhToanTable, KhoanNoTable, CongNoKhachHangForm },
  data: function () {
    return {
      tong_no: 0,
      da_thanh_toan: 0,
      con_lai: 0,
      khoan_no_column_names: [
        "Ngày xuất hàng",
        "Mã Bosch",
        "Mã Zexel",
        "Mã tem trên hộp",
        "Tên Tiếng Anh",
        "Tên Tiếng Việt",
        "Số Lượng",
        "Đơn Giá",
        "VAT",
        "Thành Tiền",
      ],
      khoan_no_resource_url:
        process.env.VUE_APP_API_ENDPOINT + "/api/v1/cong-no",
      khoan_no_column_definitions: [
        {
          data: "ngay_xuat_hang",
          render: function (data) {
            return moment(data).format("DD/MM/YYYY");
          },
        },
        { data: "bosch_no" },
        { data: "zexel_no" },
        { data: "ma_tem" },
        { data: "english_name" },
        { data: "vietnamese_name" },
        { data: "quantity" },
        { data: "price", render: $.fn.dataTable.render.number(",", ".", 2) },
        { data: "vat" },
        { data: "total", render: $.fn.dataTable.render.number(",", ".", 2) },
        {
          data: null,
          width: 100,
          defaultContent:
            '<button type="button"  action="edit" class="btn btn-warning flat ">Sửa</button>\
            <button type="button"  action="delete" class="btn btn-danger flat ">Xóa</button>',
        },
      ],
      thanh_toan_resource_url:
        process.env.VUE_APP_API_ENDPOINT + "/api/v1/cong-no-payment",
      thanh_toan_column_names: ["Ngày thanh toán", "Số tiền", "Ghi chú"],
      thanh_toan_column_definitions: [
        {
          data: "date",
          render: function (data) {
            return moment(data).format("DD/MM/YYYY");
          },
        },
        { data: "amount", render: $.fn.dataTable.render.number(",", ".", 2) },
        { data: "note" },
        {
          data: null,
          width: 100,
          defaultContent:
            '<button type="button"  action="edit"  class="btn btn-warning flat ">Sửa</button>\
            <button type="button"  action="delete" class="btn btn-danger flat ">Xóa</button>',
        },
      ],

      form_data: {},
      hide_table_footer: "true",
      title: "Công Nợ Khách Hàng",
      resource_url:
        process.env.VUE_APP_API_ENDPOINT + "/api/v1/cong-no-khach-hang",
      form: {},
      danh_sach_khach_hang: [],
      selected_khach_hang_name: "",
      selected_khach_hang_id: "",
      total_data: [],
      resource_filter: {},
      action: "Tạo",
      table: null,
      modal_name: "modal-cong-no-khach-hang-form",
    };
  },
  mounted() {
    this.get_danh_sach_khach_hang();
    $("#table_summary").DataTable({
      searching: false,
      paging: false,
      info: false,
    });
  },
  methods: {
    async get_danh_sach_khach_hang() {
      let url = this.resource_url;
      await axios.get(url).then((response) => {
        this.danh_sach_khach_hang = response.data;
      });
    },
    async render_cong_no(id = null) {
      let component = this;
      await this.get_danh_sach_khach_hang();

      if (id) {
        for (let khach_hang of this.danh_sach_khach_hang) {
          if (khach_hang && khach_hang.id === id) {
            this.selected_khach_hang_id = khach_hang.id;
            this.form = khach_hang;
            this.selected_khach_hang_name = khach_hang.name;
          }
        }
      }

      for (let khach_hang of this.danh_sach_khach_hang) {
        if (khach_hang && khach_hang.name === this.selected_khach_hang_name) {
          this.selected_khach_hang_id = khach_hang.id;
          this.form = khach_hang;
        }
      }
      let url = new URL(this.resource_url);
      url.searchParams.set("id", this.form.id);
      if (this.table) {
        this.table.ajax.url(url.href);
        this.table.ajax.reload();
      } else {
        this.table = $("#table").DataTable({
          pageLength: 50,
          ajax: {
            url: url.href,
            dataSrc: "",
          },
          searching: false,
          paging: false,
          info: false,
          columns: [
            { data: "name" },
            { data: "company" },
            { data: "address" },
            { data: "ma_so_thue" },
            { data: "note" },
            {
              data: null,
              width: 100,
              defaultContent:
                '<button type="button" action="edit" class="btn btn-warning flat">Sửa</button>\
              <button type="button" action="delete" class="btn btn-danger flat">Xóa</button>',
            },
          ],
          scrollX: false,
          autoWidth: true,
          language: {
            lengthMenu: "Hiển thị _MENU_ dòng",
          },
        });
      }

      $("#table tbody").on("click", "button", function () {
        var data = component.table.row($(this).parents("tr")).data();
        if ($(this).attr("action") == "delete") {
          component.delete_po(data.id);
          return;
        }
        component.$bvModal.show("modal-cong-no-khach-hang-form");
        component.form_data = data;
        if ("id" in data) {
          component.action = "Sửa";
        } else {
          component.action = "Tạo";
        }
      });
    },
    delete_po(id) {
      let url = new URL(this.resource_url);
      url.pathname = url.pathname + "/" + id;
      axios.delete(url.href).then(() => {
        this.$root.$bvModal.msgBoxOk(`Đã Xóa`);
        this.refresh_table_data();
      });
    },
    update_tong_no(value) {
      this.tong_no = value;
      this.con_lai = this.tong_no - this.da_thanh_toan;
    },
    update_da_thanh_toan(value) {
      this.da_thanh_toan = value;
      this.con_lai = this.tong_no - this.da_thanh_toan;
    },
    export_cong_no_excel() {
      let url = new URL(process.env.VUE_APP_API_ENDPOINT + "/api/v1/cong-no/export-excel")
      url.searchParams.set("khach_hang_id", this.selected_khach_hang_id)

      // Download file
      axios({
        url: url.href,
        method: "get",
        responseType: "blob",
      }).then((response) => {
        const url = window.URL.createObjectURL(new Blob([response.data]));
        const link = document.createElement("a");
        link.href = url;
        link.setAttribute("download", this.form.name + ".xlsx");
        document.body.appendChild(link);
        link.click();
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
th,
td {
  white-space: nowrap;
}
table.dataTable tbody th,
table.dataTable tbody td {
  padding: 0px 10px; /* e.g. change 8x to 4px here */
}

.optimize_height {
  height: 37px;
}
</style>
