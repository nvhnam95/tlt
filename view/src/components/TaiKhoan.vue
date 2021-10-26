<template>
  <div class="limit-width">
    <b-button variant="light" @click="log_out"> Đăng xuất </b-button> <br><br><br>
    <b-form @submit="update_info" v-if="show">
      <b-form-group id="input-group-1" label="User Name:" label-for="username">
        <b-form-input
          id="username"
          v-model="form.username"
          type="text"
          :locale="locale"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-1" label="Tên:" label-for="first_name">
        <b-form-input
          id="first_name"
          v-model="form.first_name"
          type="text"
          :locale="locale"
        ></b-form-input>
      </b-form-group>

      <br />
      <div style="float: right">
        <b-button type="submit" variant="light"> Cập Nhật </b-button>
      </div>
    </b-form>
    <br><br>
    <b-form @submit="update_password" v-if="show">
      <b-form-group id="input-group-1" label="Mật Khẩu Mới:" label-for="new_password">
        <b-form-input
          id="new_password"
          v-model="password_form.new_password"
          type="password"
          :locale="locale"
        ></b-form-input>
      </b-form-group>
      <b-form-group id="input-group-1" label="Nhập Lại Mật Khẩu Mới:" label-for="new_password_again">
        <b-form-input
          id="new_password_again"
          v-model="password_form.new_password_again"
          type="password"
          :locale="locale"
        ></b-form-input>
      </b-form-group>
      <br />
      <div style="float: right">
        <b-button type="submit" variant="light"> Đổi Mật Khẩu </b-button>
      </div>
    </b-form>
    
    <b-modal ok-only hide-header-close id="noti">{{noti_message}}</b-modal>
  </div>
</template>

<script>
import axios from "axios";

export default {
  async mounted() {
    await this.get_user_info();
  },
  data() {
    return {
      new_pass_string: "",
      reset_pass_string: "Reset Mật Khẩu?",
      permission_list: [],
      form: {},
      password_form: {},
      show: true,
      locale: "vi",
      noti_message: ""
    };
  },
  methods: {
    log_out(){
      localStorage.clear()
      window.location.href = "/";
    },
    async get_user_info() {
      let url = new URL(
        process.env.VUE_APP_API_ENDPOINT + "/api/v1/current-user"
      );
      await axios({
        method: "get",
        url: url,
      })
        .then((response) => {
          this.form = response.data;
        })
        .catch(function () {
          alert("Error")
        });
    },

    update_info(event) {
      event.preventDefault();
      let component = this
      let url = new URL(process.env.VUE_APP_API_ENDPOINT + "/api/v1/users");
      delete this.form.user_permissions;
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
          component.noti_message = "Cập nhật thông tin thành công"
          component.$bvModal.show("noti");
        })
        .catch(function (error) {
          alert(error);
        });
    },
    update_password(event) {
      event.preventDefault();
      let component = this;
      if (this.password_form.new_password !== this.password_form.new_password_again) {
        component.noti_message = "Mật khẩu không khớp"
        component.$bvModal.show("noti");
        return
      }
      let url = new URL(process.env.VUE_APP_API_ENDPOINT + "/api/v1/users");
      let method = "patch";
      if (this.form.id) {
        method = "patch";
        url.pathname += `/${this.form.id}/update-pass`;
      }
      axios({
        method: method,
        url: url.href,
        data: this.password_form,
      })
        .then(() => {
          component.noti_message = "Đổi mật khẩu thành công"
          component.$bvModal.show("noti");
          this.password_form = {}
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
.limit-width {
  max-width: 500px;
}
table.dataTable tbody th,
table.dataTable tbody td {
  padding: 0px 10px; /* e.g. change 8x to 4px here */
}
</style>