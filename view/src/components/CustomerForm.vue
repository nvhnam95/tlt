<template>
  <div>
    <b-form @submit="onSubmit" @close="onClose" v-if="show">
      <b-form-group id="input-group-1" label="Mã Khách Hàng:" label-for="date">
        <b-form-input
          id="code"
          v-model="form.code"
          type="text"
          :locale="locale"
        ></b-form-input>
      </b-form-group>

      <b-form-group
        id="input-group-1"
        label="Tên Khách Hàng:"
        label-for="major"
      >
        <b-form-input id="name" v-model="form.name" type="text"></b-form-input>
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