<template>
  <div>
    <h2>{{ title }}</h2>

    <div>
      <b-button @click="show_modal" variant="primary">Thêm Mới</b-button>
      &nbsp;
      <b-button
        @click="export_excel(get_serialized_total_data_info())"
        variant="primary"
        >Export Excel</b-button
      >
      <hr style="border-color: rgba(0, 0, 0, 0.1); margin: 20px" />
      <table>
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
          <td><input id="date-filter-start" /></td>
          <td><input id="date-filter-end" /></td>
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
        <component
          v-bind:is="form_name"
          @refresh_table_data="refresh_table_data"
          :resource_url_from_parent="resource_url"
          :form_data="form_data"
          :action="action"
          :modal_name_from_parent="modal_name"
          :resource_filter_from_parent="resource_filter"
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
import ChiPhiForm from "./chi_phi/ChiPhiForm.vue";
import DoanhThuBoschForm from "./chi_phi/DoanhThuBoschForm.vue";
import DoanhThuNgoaiForm from "./chi_phi/DoanhThuNgoaiForm.vue";
import CustomerForm from "./CustomerForm.vue";
import UserForm from "./UserForm.vue";
import tool_mixin from "./tool_mixins.js";
import "daterangepicker/daterangepicker";
import "daterangepicker/daterangepicker.css";

export default {
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
    "table_id_from_parent"
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
    ChiPhiForm,
    DoanhThuBoschForm,
    DoanhThuNgoaiForm,
    CustomerForm,
    UserForm
  },
  mounted() {
    let url = this.resource_url;
    this.generate_search_boxes();
    var component = this;
    this.table = $(`#${this.table_id}`).DataTable({
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
            let column_data_src = this.dataSrc();
            let allow_partial_search = [
              "pn_13",
              "english_des",
              "import_des",
              "app_des",
            ];
            $("input", this.footer()).on("keyup change clear", function () {
              if (that.search() !== this.value) {
                if (this.value === "") {
                  that.search("").draw();
                } else {
                  if (allow_partial_search.includes(column_data_src)) {
                    that.search(this.value).draw();
                  } else {
                    that.search("^" + this.value + "$", true, false).draw();
                  }
                }
              }
            });
          });
      },
      "aaSorting": [],
      drawCallback: function () {
        var api = this.api();
        for (let d of component.total_data_info) {
          d.value = api
            .columns(d.column_index, { page: "all", search: "applied" })
            .data()
            .sum()
            .toLocaleString();
        }
      },
      language: {
        lengthMenu: "Hiển thị _MENU_ dòng",
      },
      pageLength: 50
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