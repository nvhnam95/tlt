<template>
  <div>
    <b-form @submit="onSubmit" @reset="onReset" @close="onClose" v-if="show">
      <b-form-group id="input-group-1" label="PO No:" label-for="po-no">
        <b-form-input
          id="po-no"
          v-model="form.po_no"
          type="text"
        ></b-form-input>
      </b-form-group>

      <b-form-group
        id="input-group-1"
        label="Ngày Nhập:"
        label-for="input_date"
      >
        <b-form-datepicker
          id="input_date"
          v-model="form.input_date"
          type="text"
          :locale="locale"
        ></b-form-datepicker>
      </b-form-group>

      <b-form-group
        id="input-group-1"
        label="Số Chứng Từ:"
        label-for="license_no"
      >
        <b-form-input
          id="license_no"
          v-model="form.license_no"
          type="text"
        ></b-form-input>
      </b-form-group>

      <b-form-group
        id="input-group-1"
        label="Công Ty Cung Cấp:"
        label-for="provider"
      >
        <b-form-input
          id="provider"
          v-model="form.provider"
          type="text"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Pn 13:" label-for="pn-13">
        <b-form-input
          id="pn-13"
          v-model="form.pn_13"
          type="text"
          required
          v-on:input="pn_13_listener"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-3" label="Pn 10:" label-for="pn-10">
        <b-form-input
          readonly
          id="pn-10"
          type="text"
          v-model="form.pn_10"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-4" label="Bosch No:" label-for="bosch-no">
        <b-form-input
          id="bosch-no"
          v-model="form.bosch_no"
          type="text"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-5" label="Zexel No:" label-for="z-excel-no">
        <b-form-input
          id="z-excel-mo"
          v-model="form.z_exel_no"
          type="text"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-6" label="Stamping:" label-for="stamping">
        <b-form-input
          id="stamping"
          v-model="form.stamping"
          type="text"
        ></b-form-input>
      </b-form-group>

      <b-form-group
        id="input-group-8"
        label="English Description:"
        label-for="english_des"
      >
        <b-form-input
          id="english_des"
          v-model="form.english_des"
          type="text"
        ></b-form-input>
      </b-form-group>

      <b-form-group
        id="input-group-9"
        label="Import Description (Tên nhập khẩu):"
        label-for="import_des"
      >
        <b-form-input
          id="import_des"
          v-model="form.import_des"
          type="text"
        ></b-form-input>
      </b-form-group>

      <b-form-group
        id="input-group-10"
        label="App Description (Tên ứng dụng):"
        label-for="app_des"
      >
        <b-form-input
          id="app_des"
          v-model="form.app_des"
          type="text"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-11" label="Quantity:" label-for="quantity">
        <b-form-input
          id="quantity"
          v-model="form.quantity"
          type="text"
          required
          v-on:input="
            update_extension_price();
            update_tong_gia_goc();
          "
        ></b-form-input>
      </b-form-group>

      <b-form-group
        id="input-group-12"
        label="Giá Nhập DAP (USD):"
        label-for="dap_price"
      >
        <b-form-input
          id="dap_price"
          v-model="form.dap_price"
          type="text"
          required
          v-on:input="
            update_extension_price();
            update_gia_goc();
          "
        ></b-form-input>
      </b-form-group>

      <b-form-group
        id="input-group-13"
        label="Extension Price (USD):"
        label-for="extension_price"
      >
        <b-form-input
          readonly
          id="extension_price"
          v-model="form.extension_price"
          type="text"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-14" label="Thuế (VAT+TNK):" label-for="tax">
        <b-form-input
          id="tax"
          v-model="form.tax"
          type="text"
          required
          v-on:input="update_gia_goc"
        ></b-form-input>
      </b-form-group>

      <b-form-group
        id="input-group-15"
        label="Giá vốn/Giá khởi điểm (VND):"
        label-for="gia_von"
      >
        <b-form-input
          id="gia_von"
          v-model="form.gia_von"
          type="text"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group
        id="input-group-16"
        label="Giá sỉ (VND):"
        label-for="gia_si"
      >
        <b-form-input
          id="gia_si"
          v-model="form.gia_si"
          type="text"
          required
          v-on:input="update_gia_le"
        ></b-form-input>
      </b-form-group>

      <b-form-group
        id="input-group-16"
        label="Giá Bán Lẻ (VND):"
        label-for="gia_le"
      >
        <b-form-input
          readonly
          id="gia_le"
          v-model="form.gia_le"
          type="text"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group
        id="input-group-16"
        label="Giá Gốc (VND):"
        label-for="gia_goc"
      >
        <b-form-input
          readonly
          id="gia_goc"
          v-model="form.gia_goc"
          type="text"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group
        id="input-group-16"
        label="Tổng Giá Gốc (VND):"
        label-for="tong_gia_goc"
      >
        <b-form-input
          readonly
          id="tong_gia_goc"
          v-model="form.tong_gia_goc"
          type="text"
          required
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-16" label="Tỷ Giá:" label-for="ratio">
        <b-form-input
          id="ratio"
          v-model="form.ratio"
          type="text"
          required
          v-on:input="update_gia_goc"
        ></b-form-input>
      </b-form-group>

      <b-form-group
        id="input-group-16"
        label="% VAT:"
        label-for="vat_percentage"
      >
        <b-form-input
          id="vat_percentage"
          v-model="form.vat_percentage"
          type="text"
        ></b-form-input>
      </b-form-group>

      <b-form-group
        id="input-group-17"
        label="Khách Hàng:"
        label-for="remark"
      >
        <b-form-input
          id="remark"
          v-model="form.remark"
          type="text"
        ></b-form-input>
      </b-form-group>

      <br />
      <div style="float: right">
        <b-button type="submit" variant="light">{{ action }} </b-button>
        <b-button type="reset" variant="light">Reset </b-button>
        <b-button @click="onClose" variant="light">Đóng</b-button>
      </div>
    </b-form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: ["form_data", "action"],
  data() {
    return {
      form: Object.keys(this.$props["form_data"]).length !== 0 ? this.$props["form_data"] : {
        provider: "Bosch",
        bosch_no: "",
        z_exel_no: "",
        english_des: "",
      },
      show: true,
      locale: "vi"
    };
  },
  methods: {
    pn_13_listener() {
      this.form.pn_10 = this.form.pn_13.slice(0, 10);
      this.update_bosch_no_zexel_stamping_based_on_pn_10();
    },
    update_extension_price() {
      if (this.form.quantity && this.form.dap_price) {
        this.form.extension_price = this.form.quantity * this.form.dap_price;
      }
    },
    update_gia_le() {
      if (this.form.gia_si) {
        this.form.gia_le = parseFloat(this.form.gia_si * 1.1).toFixed(2);
      } else {
        this.form.gia_le = "";
      }
    },
    update_gia_goc() {
      if (this.form.dap_price && this.form.ratio && this.form.tax) {
        this.form.gia_goc = parseFloat(
          this.form.dap_price * this.form.ratio * this.form.tax
        ).toFixed(2);
        this.update_tong_gia_goc();
      } else {
        this.form.gia_goc = "";
      }
    },
    update_tong_gia_goc() {
      if (this.form.gia_goc && this.form.quantity) {
        this.form.tong_gia_goc = parseFloat(
          this.form.gia_goc * this.form.quantity
        ).toFixed(2);
      } else {
        this.form.tong_gia_goc = "";
      }
    },
    update_bosch_no_zexel_stamping_based_on_pn_10() {
      let params = { pn_13: this.form.pn_13 };
      let base_url = process.env.VUE_APP_API_ENDPOINT;
      let url = base_url + "/api/v1/purchasing-orders";

      axios.get(url, { params }).then((response) => {
        if (response.data.length > 0) {
          var po = response.data[0];
          this.form.bosch_no = po.bosch_no;
          this.form.z_exel_no = po.z_exel_no;
          this.form.stamping = po.stamping;
          this.form.english_des = po.english_des;
          this.form.app_des = po.app_des;
          this.form.import_des = po.import_des;
        }
        else {
          this.form.bosch_no = "";
          this.form.z_exel_no = "";
          this.form.stamping = "";
          this.form.english_des = "";
          this.form.app_des = "";
          this.form.import_des = "";
        }
      });
    },
    onSubmit(event) {
      event.preventDefault();
      let component = this;
      let base_url = process.env.VUE_APP_API_ENDPOINT;
      let url = base_url + "/api/v1/nhap-kho";
      let method = "post";
      if (this.form.id) {
        method = "put";
        url = `${url}/${this.form.id}`;
      }
      axios({
        method: method,
        url: url,
        data: this.form,
      })
        .then(() => {
          component.$root.$emit("bv::hide::modal", "modal-nhap-kho-form", "#btnShow");
          component.$root.$bvModal.msgBoxOk(`Đã ${this.$props["action"]}`);
          component.$emit("refresh_table_data");
        })
        .catch(function (error) {
          alert(error);
        });
    },
    onReset(event) {
      event.preventDefault();
      // Reset our form values
      this.form = {};
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
        this.form.provider = "Bosch";
      });
    },
    onClose() {
      this.$root.$emit("bv::hide::modal", "modal-nhap-kho-form", "#btnShow");
      this.$emit("refresh_table_data");
    },
  },
};
</script>

<style>
button {
  padding: 5px;
}
table.dataTable tbody th, table.dataTable tbody td {
    padding: 0px 10px; /* e.g. change 8x to 4px here */
}
</style>