<template>
  <div>
    <h2>{{ title }}</h2>

    <div>
      <b-button @click="show_modal" variant="primary">Thêm Mới</b-button>
      &nbsp;
      <hr style="border-color: rgba(0, 0, 0, 0.1); margin: 20px" />
      <table v-if="false">
        <tr>
          <th>Từ Ngày</th>
          <th>Đến ngày</th>
          <th></th>
          <th
            class="px-5"
            v-for="item in total_data_info"
            v-bind:key="item.name"
          >
            {{ item.name }}
          </th>
        </tr>
        <tr>
          <td><input id="date-filter-start-khoan-no" /></td>
          <td><input id="date-filter-end-khoan-no" /></td>
          <td></td>
          <td
            class="px-5"
            v-for="item in total_data_info"
            v-bind:key="item.name"
          >
            {{ item.value }} {{ item.suffix }}
          </td>
        </tr>
      </table>
      <br />
      <b-modal :id="modal_name" no-close-on-backdrop hide-header-close>
        <KhoanNoForm
          @refresh_table_data="refresh_table_data"
          :resource_url_from_parent="resource_url"
          :form_data="form_data"
          :action="action"
          :modal_name_from_parent="modal_name"
          :resource_filter_from_parent="resource_filter"
          :khach_hang_id_from_parent="khach_hang_id_from_parent"
        />
        <template #modal-footer>
          <br />
        </template>
      </b-modal>
    </div>
    <table
      class="table table-hover table-bordered cell-border stripe"
      v-bind:id="table_id"
    >
      <thead>
        <tr>
          <th v-for="item in column_names" v-bind:key="item">{{ item }}</th>
          <th style="min-width: 100px" ></th>
        </tr>
      </thead>
      <tfoot v-if=!hide_table_footer>
        <tr >
          <th v-for="item in column_names" v-bind:key="item">{{ item }}</th>
        </tr>
      </tfoot>
    </table>
  </div>
</template>

<script>
import $ from "jquery";

import axios from "axios";
import KhoanNoForm from "./KhoanNoForm.vue";
import tool_mixin from "../tool_mixins.js";
import "daterangepicker/daterangepicker";
import "daterangepicker/daterangepicker.css";
import moment from "moment";

export default {
  watch: {
    khach_hang_id_from_parent(){
      this.refresh_table_data()
    }
  },
  mixins: [tool_mixin],
  props: [
    "title",
    "column_names",
    "columns",
    "total_data_from_parent",
    "resource_url_from_parent",
    "form_name_from_parent",
    "modal_name_from_parent",
    "resource_filter_from_parent",
    "export_file_name_from_parent",
    "hide_table_footer_from_parent",
    "table_id_from_parent",
    "khach_hang_id_from_parent"
  ],
  data: function () {
    return {
      table: null,
      form_data: {
        provider: "Bosch",
        gia_goc: "",
        gia_si: "",
        gia_le: "",
        tien_goc: "",
      },
      action: "Tạo",
      column_definitions: this.$props["columns"],
      total_data_info: this.$props["total_data_from_parent"],
      resource_url: this.$props["resource_url_from_parent"],
      form_name: this.$props["form_name_from_parent"],
      modal_name: this.$props["modal_name_from_parent"],
      table_id: "table_id_from_parent" in this.$props && this.$props["table_id_from_parent"] ? this.$props["table_id_from_parent"] : "poes_table",
      resource_filter:
        Object.keys(this.$props["resource_filter_from_parent"]).length !== 0
          ? this.$props["resource_filter_from_parent"]
          : {},
      export_file_name: this.$props["export_file_name_from_parent"],
      hide_table_footer: "hide_table_footer_from_parent" in this.$props && this.$props["hide_table_footer_from_parent"] === "true" ? true : false,
      date_filter_start: null,
      date_filter_end: null,
    };
  },
  components: {
    KhoanNoForm
  },
  mounted() {
    let url = new URL(this.resource_url);
    url.searchParams.set("khach_hang", this.khach_hang_id_from_parent)
    this.generate_search_boxes();
    var component = this;
    this.table = $(`#${this.table_id}`).DataTable({
      pageLength: 50,
      ajax: {
        url: url.href,
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
      "aaSorting": [],
      language: {
        lengthMenu: "Hiển thị _MENU_ dòng",
      },
      drawCallback: function () {
        var api = this.api();
        component.$emit("update_tong_no", api.column( 9, {page:'all', search: 'applied'} ).data().sum())
      },
    });

    $(`#${this.table_id} tfoot th`).each(function () {
      var title = $(this).text();
      $(this).html('<input type="text" placeholder="Tìm ' + title + '" />');
    });

    $(`#${this.table_id} tbody`).on("click", "button", function () {
      var data = component.table.row($(this).parents("tr")).data();
      if ($(this).attr("action") == "delete") {
        component.delete_po(data.id);
        return;
      }
      component.$bvModal.show(component.modal_name);
      component.form_data = data;
      if ("id" in data) {
        component.action = "Sửa";
      } else {
        component.action = "Tạo";
      }
    });
  },
  methods: {
          generate_search_boxes() {
            let table_id = this.table_id || "poes_table"
            $(`#${table_id} tfoot th`).each(function () {
              var title = $(this).text();
              $(this).html('<input type="text" placeholder="Tìm ' + title + '" />');
            });
      
            // Date range
            var start = moment();
            var end = moment();
            $("#date-filter-start-khoan-no").daterangepicker(
              {
                singleDatePicker: true,
                locale: {
                  format: "DD/MM/YYYY",
                  separator: " - ",
                  applyLabel: "OK",
                  cancelLabel: "Hủy",
                  fromLabel: "Từ",
                  toLabel: "Đến",
                  customRangeLabel: "Chọn khoảng thời gian",
                  weekLabel: "W",
                  daysOfWeek: ["CN", "T2", "T3", "T4", "T5", "T5", "T7"],
                  monthNames: [
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
                    "Tháng 12",
                  ],
                  firstDay: 1,
                },
              },
              this.date_range_filter_callback_for_start
            );
      
            $("#date-filter-end-khoan-no").daterangepicker(
              {
                singleDatePicker: true,
                startDate: start,
                endDate: end,
                locale: {
                  format: "DD/MM/YYYY",
                  separator: " - ",
                  applyLabel: "OK",
                  cancelLabel: "Hủy",
                  fromLabel: "Từ",
                  toLabel: "Đến",
                  customRangeLabel: "Chọn khoảng thời gian",
                  weekLabel: "W",
                  daysOfWeek: ["CN", "T2", "T3", "T4", "T5", "T5", "T7"],
                  monthNames: [
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
                    "Tháng 12",
                  ],
                  firstDay: 1,
                },
              },
              this.date_range_filter_callback_for_end
            );
            $('input[id="date-filter-start-khoan-no"]').val("")
            $('input[id="date-filter-end-khoan-no"]').val("")
          },
    get_serialized_total_data_info() {
      // Return a list of list
      if (this.total_data_info.length) {
        let res = [];
        for (let d of this.total_data_info) {
          res.push([d.name, d.value]);
        }
        return res;
      } else return [];
    },
    show_modal() {
      this.form_data = {};
      this.$bvModal.show(this.modal_name);
    },
    delete_po(id) {
      let url = new URL(this.resource_url);
      url.pathname = url.pathname + "/" + id;
      axios.delete(url.href).then(() => {
        this.$root.$bvModal.msgBoxOk(`Đã Xóa`);
        this.refresh_table_data();
      });
    },
    refresh_table_data(){
      let url = new URL(this.table.ajax.url())
      url.searchParams.set("khach_hang", this.khach_hang_id_from_parent)
      this.table.ajax.url(url.href);
      this.table.ajax.reload();
    }
  },
};
</script>

<style scoped>
table.dataTable thead th {
  white-space: nowrap;
}
table.dataTable {
  width: 100%;
  margin: 0 !important;
}
</style>