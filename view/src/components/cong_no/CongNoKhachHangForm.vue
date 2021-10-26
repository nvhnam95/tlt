<template>
  <div>
    <b-form @submit="onSubmit" @close="onClose" v-if="show">

      <b-form-group id="input-group-1" label="Tên:" label-for="name">
        <b-form-input
          id="name"
          v-model="form.name"
          type="text"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-1" label="Công Ty:" label-for="amount">
        <b-form-input
          id="company"
          v-model="form.company"
          type="text"
        ></b-form-input>
      </b-form-group>

      <b-form-group
        id="client_code"
        label="Địa Chỉ:"
        label-for="address"
      >
        <b-form-input
          id="address"
          v-model="form.address"
          type="text"
        ></b-form-input>
      </b-form-group>
      
      <b-form-group
        id="client_code"
        label="Mã Số Thuế:"
        label-for="ma_so_thue"
      >
        <b-form-input
          id="ma_so_thue"
          v-model="form.ma_so_thue"
          type="text"
        ></b-form-input>
      </b-form-group>
      
      <b-form-group
        id="client_code"
        label="Ghi Chú:"
        label-for="note"
      >
        <b-form-input
          id="note"
          v-model="form.note"
          type="text"
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
  props: ["form_data", "action", "resource_url_from_parent", 
  "modal_name_from_parent", "resource_filter_from_parent",
  ],
  data() {
    return {
      form:
        Object.keys(this.$props["form_data"]).length !== 0
          ? this.$props["form_data"]
          : {
            
          },
      show: true,
      locale: "vi",
      resource_url: this.$props["resource_url_from_parent"],
      modal_name: this.$props["modal_name_from_parent"],
    }
  },
  methods: {
    async onSubmit(event) {
      event.preventDefault();
      let component = this;

      let url = new URL(this.resource_url);
      let method = "post";
      if (this.form.id) {
        method = "put";
        url.pathname += `/${this.form.id}`
      }
      await axios({
        method: method,
        url: url.href,
        data: this.form,
      })
        .then((response) => {
          this.$emit("render_cong_no", response.data.id);
          component.$root.$emit(
            "bv::hide::modal",
            component.modal_name,
            "#btnShow"
          );
          component.$root.$bvModal.msgBoxOk(
            `Đã ${this.$props["action"]}`
          );
          component.$emit("refresh_table_data");
        })
        .catch(function (error) {
          alert(error);
        });
    },
    onClose() {
      this.$root.$emit(
        "bv::hide::modal",
        this.modal_name,
        "#btnShow"
      );
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