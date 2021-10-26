<template>
  <div>
    <b-form @submit="onSubmit" @close="onClose" v-if="show">
      <b-form-group id="input-group-1" label="User Name:" label-for="username">
        <b-form-input
          id="username"
          v-model="form.username"
          type="text"
          :locale="locale"
        ></b-form-input>
      </b-form-group>
      <br />
      <b-form-group id="input-group-1" label="Tên:" label-for="first_name">
        <b-form-input
          id="first_name"
          v-model="form.first_name"
          type="text"
          :locale="locale"
        ></b-form-input>
      </b-form-group>
<br />
      <b-form-group v-if=!form.id id="input-group-1" label="Mật Khẩu:" label-for="password">
        <b-form-input
          id="password"
          v-model="form.password"
          type="password"
          :locale="locale"
        ></b-form-input>
      </b-form-group>

      <br />
      <b-form-group id="input-group-1" label="Quyền:" label-for="major">
        <b-form-checkbox
          v-for="permission in permission_list"
          v-model="permissions"
          :key="permission.name"
          :value="permission.codename"
        >
          &nbsp; {{ permission.name }}
        </b-form-checkbox>
        <br />
      </b-form-group>
      <b-button v-if="form.id" @click="reset_mat_khau" variant="light"> Reset Mật Khẩu </b-button>
      <br />
      <div style="float: right">

        <b-button type="submit" variant="light">OK </b-button>
        <b-button @click="onClose" variant="light">Đóng</b-button>
      </div>
      <div>
        <b-modal hide-header-close @ok="send_reset_pass_request" id="reset-pass-modal">{{reset_pass_string}}</b-modal>
        <b-modal hide-header-close id="new-pass-modal">{{new_pass_string}}</b-modal>
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
  async mounted() {
    await this.get_permissions();
  },
  data() {
    return {
      new_pass_string: "",
      reset_pass_string: "Reset Mật Khẩu?",
      permission_list: [],
      form:
        Object.keys(this.$props["form_data"]).length !== 0
          ? this.$props["form_data"]
          : {"permissions": []},
      permissions: "user_permissions" in this.$props["form_data"] ? this.$props["form_data"].user_permissions : [],
      show: true,
      locale: "vi",
      resource_url: this.$props["resource_url_from_parent"],
      modal_name: this.$props["modal_name_from_parent"],
    }
  },
  methods: {
    reset_mat_khau(){
      this.$bvModal.show("reset-pass-modal");
    },
    async send_reset_pass_request(){
      let url = new URL(process.env.VUE_APP_API_ENDPOINT + "/api/v1/users/" + this.form.id + "/" + "reset-pass")
      await axios({
        method: "get",
        url: url.href,
      })
        .then((response) => {
          this.new_pass_string = "Mật khẩu mới: " + response.data.password;
          this.$bvModal.show("new-pass-modal");
        })
        .catch(function () {
          alert("Không thể reset mật khẩu")
        });
    },
    async get_permissions() {
      let url = new URL(
        process.env.VUE_APP_API_ENDPOINT + "/api/v1/current-user"
      );
      await axios({
        method: "get",
        url: url,
      })
        .then((response) => {
          this.form.permissions = response.data.permissions;
        })
        .catch(function () {
          localStorage.removeItem("is_authenticated");
          localStorage.removeItem("token");
          this.$router.push("Login");
        });

      url = new URL(
        process.env.VUE_APP_API_ENDPOINT + "/api/v1/users/all-permissions"
      );
      await axios({
        method: "get",
        url: url,
      })
        .then((response) => {
          this.permission_list = response.data;
        })
        .catch(function () {
          localStorage.removeItem("is_authenticated");
          localStorage.removeItem("token");
          this.$router.push("Login");
        });
    },

    onSubmit(event) {
      event.preventDefault();
      let component = this;
      let url = new URL(this.resource_url);
      delete this.form.user_permissions;
      this.form.permissions = this.permissions;
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
          component.$root.$bvModal.msgBoxOk(`Thành công`);
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