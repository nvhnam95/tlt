<template>
  <div>
    <b-form @submit="onSubmit" @reset="onReset" @close="onClose" v-if="show">
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

      <b-form-group id="input-group-2" label="Pn 13:" label-for="pn-13">
        <b-form-input
          id="pn_13"
          v-model="form.pn_13"
          type="text"
          required
          v-on:input="update_gia_goc_descriptions"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-11" label="Quantity:" label-for="quantity">
        <b-form-input
          id="quantity"
          v-model="form.quantity"
          type="text"
          required
          v-on:input="update_tien_goc()"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-3" label="Giá Gốc:" label-for="gia_goc">
        <b-form-input
          readonly
          id="gia_goc"
          type="text"
          v-model="form.gia_goc"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-3" label="Tiền Gốc:" label-for="tien_goc">
        <b-form-input
          readonly
          id="tien_goc"
          type="text"
          v-model="form.tien_goc"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-3" label="Giá Bán Sỉ:" label-for="gia_si">
        <b-form-input
          readonly
          id="gia_si"
          type="text"
          v-model="form.gia_si"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-3" label="Giá Bán Lẻ:" label-for="gia_le">
        <b-form-input
          readonly
          id="gia_le"
          type="text"
          v-model="form.gia_le"
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
        label="Import Description (Tên Nhập Khẩu):"
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
        label="App Description (Tên Ứng Dụng):"
        label-for="app_des"
      >
        <b-form-input
          id="app_des"
          v-model="form.app_des"
          type="text"
        ></b-form-input>
      </b-form-group>

      <b-form-group
        id="input-group-12"
        label="Khách Hàng:"
        label-for="customer"
      >
        <b-form-input
          id="customer"
          v-model="form.customer"
          type="text"
        ></b-form-input>
      </b-form-group>

      <br />
      <div style="float: right">
        <b-button type="submit" variant="light">{{action}} </b-button>
        <b-button type="reset" variant="light">Reset </b-button>
        <b-button @click="onClose" variant="light">Đóng</b-button>
      </div>
    </b-form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: 
    ['form_data', 'action'], 
  data() {
    return {
      form: Object.keys(this.$props["form_data"]).length !== 0 ? this.$props["form_data"] : {
        provider: "Bosch",
        gia_goc: "",
        gia_si: "",
        gia_le: "",
        tien_goc: "",
      },
      show: true,
      locale: "vi"
    };
  },
  methods: {
    update_tien_goc() {
      if (this.form.quantity && this.form.gia_goc) {
        this.form.tien_goc = parseFloat(
          this.form.quantity * this.form.gia_goc
        ).toFixed(2);
      } else {
        this.form.tien_goc = "";
      }
    },
    update_gia_goc_descriptions() {
      let params = { pn_13: this.form.pn_13 };
      let base_url = process.env.VUE_APP_API_ENDPOINT
      let url = base_url + "/api/v1/nhap-kho"
      axios({
        method: 'get',
        url: url,
        params: params
      }).then((response) => {
          if (response.data.length > 0) {
            var nhap_kho = response.data[0];
            this.form.gia_si = nhap_kho.gia_si;
            this.form.gia_le = nhap_kho.gia_le;
            this.form.english_des = nhap_kho.english_des;
            this.form.import_des = nhap_kho.import_des;
            this.form.app_des = nhap_kho.app_des;
          } else {
            this.form.gia_si = "";
            this.form.gia_le = "";
            this.form.english_des = "";
            this.form.import_des = "";
            this.form.app_des = "";
          }
        });

      url = base_url + "/api/v1/xuat-kho/calculate-gia-goc"
      params.id = this.form.id
      params.input_date = this.form.input_date
      axios({
        method: 'get',
        url: url,
        params: params
      }).then((response) => {
          this.form.gia_goc = response.data;
          this.update_tien_goc();
        });
      
    },
    onSubmit(event) {
      event.preventDefault()
      let component = this
      let base_url = process.env.VUE_APP_API_ENDPOINT
      let url = base_url + "/api/v1/xuat-kho"
      let method = 'post'
      if (this.form.id) {
        method = 'put'
        url = `${url}/${this.form.id}`
      }
      axios({
        method: method,
        url: url,
        data: this.form
      }).then(() => {
          component.$root.$emit("bv::hide::modal", "modal-xuat-kho-form", "#btnShow");
        component.$root.$bvModal.msgBoxOk(`Đã ${this.$props['action']} Xuất Kho`)
        component.$emit('refresh_table_data')
        })
        .catch(function (error) {
          alert(error);
        });
    },
    onReset(event) {
      event.preventDefault();
      this.form = {};
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
        this.form.provider = "Bosch";
      });
    },
    onClose() {
      this.$root.$emit('bv::hide::modal', 'modal-xuat-kho-form', "#btnShow")
      this.$emit('refresh_table_data')
    },
  },
};
</script>

<style>
button {
  padding: 5px;
}
</style>