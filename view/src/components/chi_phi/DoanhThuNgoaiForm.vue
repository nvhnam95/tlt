<template>
  <div>
    <b-form @submit="onSubmit" @close="onClose" v-if="show">
      <b-form-group id="input-group-1" label="Ngày:" label-for="date">
        <b-form-datepicker
          id="date"
          v-model="form.date"
          type="text"
          :locale="locale"
        ></b-form-datepicker>
      </b-form-group>

      <b-form-group id="input-group-1" label="Mã Khách Hàng:" label-for="client_code">
        <b-form-input
          id="client_code"
          v-model="form.client_code"
          type="text"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="accessory_code" label="Mã Phụ Tùng:" label-for="accessory_code">
        <b-form-input
          id="accessory_code"
          v-model="form.accessory_code"
          type="text"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Số Lượng:" label-for="quantity">
        <b-form-input
          id="quantity"
          v-model="form.quantity"
          type="text"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-3" label="Giá Vốn:" label-for="gia_von">
        <b-form-input
          id="gia_von"
          type="text"
          v-model="form.gia_von"
        ></b-form-input>
      </b-form-group>


      <b-form-group id="input-group-3" label="Tiền Vốn:" label-for="tien_von">
        <b-form-input
          id="tien_von"
          type="text"
          v-model="form.tien_von"
        ></b-form-input>
      </b-form-group>
      
      <b-form-group id="input-group-3" label="Giá Bán:" label-for="gia_ban">
        <b-form-input
          id="gia_ban"
          type="text"
          v-model="form.gia_ban"
        ></b-form-input>
      </b-form-group>
      
      <b-form-group id="input-group-3" label="Tiền Bán:" label-for="tien_ban">
        <b-form-input
          id="tien_ban"
          type="text"
          v-model="form.tien_ban"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-3" label="Nội Dung:" label-for="content">
        <b-form-input
          id="content"
          type="text"
          v-model="form.content"
        ></b-form-input>
      </b-form-group>

      <br />

      <div style="float: right">
        <b-button type="submit" variant="light">{{ action }} </b-button>
        <b-button @click="onClose" variant="light">Đóng</b-button>
      </div>
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
  ],
  data() {
    return {
      form:
        Object.keys(this.$props["form_data"]).length !== 0
          ? this.$props["form_data"]
          : {
              cost_type: this.$props["resource_filter_from_parent"].cost_type,
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
  },
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