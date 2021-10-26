<template>
  <div>
    <b-form @submit="onSubmit" @close="onClose" v-if="show">
      <b-form-group
        id="input-group-1"
        label="Ngày xuất hàng:"
        label-for="ngay_xuat_hang"
      >
        <b-form-datepicker
          id="ngay_xuat_hang"
          v-model="form.ngay_xuat_hang"
          type="text"
          :locale="locale"
        ></b-form-datepicker>
      </b-form-group>

      <b-form-group id="input-group-1" label="Bosch No:" label-for="bosch_no">
        <b-form-input
          id="bosch_no"
          v-model="form.bosch_no"
          type="text"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="client_code" label="Zecel No:" label-for="zexel_no">
        <b-form-input
          id="zexel_no"
          v-model="form.zexel_no"
          type="text"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Mã Tem:" label-for="ma_tem">
        <b-form-input
          id="ma_tem"
          v-model="form.ma_tem"
          type="text"
        ></b-form-input>
      </b-form-group>

      <b-form-group
        id="input-group-3"
        label="Tên Tiếng Anh:"
        label-for="english_name"
      >
        <b-form-input
          id="english_name"
          type="text"
          v-model="form.english_name"
        ></b-form-input>
      </b-form-group>
      <b-form-group
        id="input-group-3"
        label="Tên Tiếng Việt:"
        label-for="vietnamese_name"
      >
        <b-form-input
          id="vietnamese_name"
          type="text"
          v-model="form.vietnamese_name"
        ></b-form-input>
      </b-form-group>
      <b-form-group id="input-group-3" label="Số Lượng:" label-for="quantity">
        <b-form-input
          id="quantity"
          type="text"
          v-model="form.quantity"
        ></b-form-input>
      </b-form-group>
      <b-form-group id="input-group-3" label="Đơn Giá:" label-for="price">
        <b-form-input
          id="price"
          type="text"
          v-model="form.price"
        ></b-form-input>
      </b-form-group>
      <b-form-group id="input-group-3" label="VAT:" label-for="vat">
        <b-form-input id="vat" type="text" v-model="form.vat"></b-form-input>
      </b-form-group>
      <b-form-group id="input-group-3" label="Thành Tiền:" label-for="total">
        <b-form-input
          id="total"
          type="text"
          v-model="form.total"
        ></b-form-input>
        
      </b-form-group>
      <br />
      <div style="float: right">
        <b-button type="submit" variant="light">{{ action }} </b-button>
        <b-button @click="onClose" variant="light">Đóng</b-button>
      </div>
      <input type="hidden" name="khach_hang" :value="form.khach_hang">
    </b-form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  
  name: "chi-phi-quan-ly-form",
  props: [
    "form_data",
    "action",
    "resource_url_from_parent",
    "modal_name_from_parent",
    "resource_filter_from_parent",
    "khach_hang_id_from_parent",
  ],
  data() {
    return {
      form:
        Object.keys(this.$props["form_data"]).length !== 0
          ? this.$props["form_data"]
          : {
              khach_hang: this.$props["khach_hang_id_from_parent"],
            },
      show: true,
      locale: "vi",
      resource_url: this.$props["resource_url_from_parent"],
      modal_name: this.$props["modal_name_from_parent"],
    };
  },
  methods: {
    onSubmit(event) {
      event.preventDefault();
      let component = this;
      let url = new URL(this.resource_url);

      let method = "post";
      if (this.form.id) {
        method = "put";
        url.pathname += `/${this.form.id}`;
      }
      axios({
        method: method,
        url: url.href,
        data: this.form,
      })
        .then(() => {
          component.$root.$emit(
            "bv::hide::modal",
            component.modal_name,
            "#btnShow"
          );
          component.$root.$bvModal.msgBoxOk(`Đã ${this.$props["action"]}`);
          component.$emit("refresh_table_data");
        })
        .catch(function (error) {
          alert(error);
        });
    },
    onClose() {
      this.$root.$emit("bv::hide::modal", this.modal_name, "#btnShow");
      this.$emit("refresh_table_data");
    },
  }

};
</script>

<style>
button {
  padding: 5px;
}
table.dataTable tbody th,
table.dataTable tbody td {
  padding: 0px 10px; /* e.g. change 8x to 4px here */
}
</style>