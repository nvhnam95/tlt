<template>
  <div>
    <b-form @submit="onSubmit" @reset="onReset" @close="onClose" v-if="show">
      <b-form-group
        id="input-group-1"
        label="Ngày Nhập:"
        label-for="input_date"
      >
        <b-form-input
          id="input_date"
          v-model="form.input_date"
          type="text"
          required
        ></b-form-input>
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

      <b-form-group
        id="input-group-8"
        label="English Description:"
        label-for="english_des"
      >
        <b-form-input
          id="english_des"
          v-model="form.english_des"
          type="text"
          required
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
          required
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
          required
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
          required
        ></b-form-input>
      </b-form-group>

      <br />
      <div style="float: right">
        <b-button type="submit" variant="light">Tạo </b-button>
        <b-button type="reset" variant="light">Reset </b-button>
        <b-button @click="onClose" variant="light">Đóng</b-button>
      </div>
    </b-form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      form: {
        provider: "Bosch",
        gia_goc: ""
      },
      show: true,
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
    
      axios
        .get("http://localhost:8000/api/v1/nhap-kho", { params })
        .then((response) => {
          if (response.data.length > 0) {
            var nhap_kho = response.data[0];
            console.log(nhap_kho);
            this.form.gia_goc = nhap_kho.gia_goc;
            this.form.english_des = nhap_kho.english_des;
            this.form.import_des = nhap_kho.import_des;
            this.form.app_des = nhap_kho.app_des;
          } else {
            this.form.gia_goc = "";
            this.form.english_des = "";
            this.form.import_des = "";
            this.form.app_des = "";
          }
          this.update_tien_goc();
          // this.form.$emit('input', '?')
        });
    },
    onSubmit(event) {
      event.preventDefault();
      let thiz = this.$root;
      axios
        .post("http://localhost:8000/api/v1/xuat-kho", this.form)
        .then((response) => {
          console.log(response);
          thiz.$emit("bv::hide::modal", "modal-po-form", "#btnShow");
          thiz.$bvModal.msgBoxOk("Đã tạo xuất kho");
          window.location.reload();
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
      this.$root.$emit("bv::hide::modal", "modal-po-form", "#btnShow");
      window.location.reload();
    },
  },
};
</script>

<style>
button {
  padding: 5px;
}
</style>