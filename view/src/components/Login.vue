<template>
  <div>
    <div class="container-fluid">
      <div class="row main-content bg-success text-center">
        <div class="col-md-4 text-center company__info">
          <span class="company__logo"
            ><h2><span class="fa fa-cart-plus"></span></h2
          ></span>
          <h4 class="company_title">
            TLT INTERNATIONAL ENGINEERING TECHNOLOGY CO.,LTD
          </h4>
        </div>
        <div class="col-md-8 col-xs-12 col-sm-12 login_form">
          <div class="container-fluid">
            <div class="row">
              <h2>Log In</h2>
            </div>
            <div class="row">
              <b-form @submit="onSubmit">
                <b-form-input
                  id="input-1"
                  v-model="form.username"
                  type="text"
                  placeholder="Tài khoản"
                  required
                  v-on:input="is_failed=false"
                ></b-form-input
                ><br />

                <b-form-input
                  id="input-1"
                  v-model="form.password"
                  type="password"
                  placeholder="Mật khẩu"
                  required
                  v-on:input="is_failed=false"
                ></b-form-input>

                <b-alert v-model="is_failed" variant="danger">{{message}}</b-alert>

                <!-- <span style="float: left, color:red" v-if="is_failed">{{message}}</span> -->


                <div style="float: left">
                  <b-button @click="onSubmit" variant="light">Đăng nhập</b-button>
                </div>
              </b-form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import $ from "jquery";
import axios from "axios";

export default {
  mounted() {
    $(".v-sidebar-menu").hide();
    if (localStorage.getItem("is_authenticated"))
      window.location.href = "/";
  },
  data() {
    return {
      message: "",
      is_failed: false,
      form: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
    onSubmit(event) {
      let component = this
      event.preventDefault();
      let base_url = process.env.VUE_APP_API_ENDPOINT;
      let url = base_url + "/api-token-auth/";
      let method = "post";
      if (this.form.id) {
        method = "put";
        url = `${url}/${this.form.id}`;
      }
      axios({
        method: method,
        url: url,
        data: component.form,
      })
        .then((response) => {
          localStorage.setItem("token", response.data.token)
          localStorage.setItem("is_authenticated", true)
          
          location.reload()
        })
        .catch(function () {
          component.is_failed = true
          component.message = "Sai tài khoản hoặc mật khẩu"
        });
    },
  },
};
</script>

<style scoped>
.main-content {
  width: 50%;
  border-radius: 20px;
  box-shadow: 0 5px 5px rgba(0, 0, 0, 0.4);
  margin: 5em auto;
  display: flex;
}
.company__info {
  background-color: #008080;
  border-top-left-radius: 20px;
  border-bottom-left-radius: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  color: #fff;
}
.fa-android {
  font-size: 3em;
}
@media screen and (max-width: 640px) {
  .main-content {
    width: 90%;
  }
  .company__info {
    display: none;
  }
  .login_form {
    border-top-left-radius: 20px;
    border-bottom-left-radius: 20px;
  }
}
@media screen and (min-width: 642px) and (max-width: 800px) {
  .main-content {
    width: 70%;
  }
}
.row > h2 {
  color: #008080;
}
.login_form {
  background-color: #fff;
  border-top-right-radius: 20px;
  border-bottom-right-radius: 20px;
  border-top: 1px solid #ccc;
  border-right: 1px solid #ccc;
}
form {
  padding: 0 2em;
}
.form__input {
  width: 100%;
  border: 0px solid transparent;
  border-radius: 0;
  border-bottom: 1px solid #aaa;
  padding: 1em 0.5em 0.5em;
  padding-left: 2em;
  outline: none;
  margin: 1.5em auto;
  transition: all 0.5s ease;
}
.form__input:focus {
  border-bottom-color: #008080;
  box-shadow: 0 0 5px rgba(0, 80, 80, 0.4);
  border-radius: 4px;
}
.btn {
  transition: all 0.5s ease;
  /* width: 70%; */
  border-radius: 30px;
  color: #008080;
  font-weight: 600;
  background-color: #fff;
  border: 1px solid #008080;
  margin-top: 1.5em;
  margin-bottom: 1em;
}
.btn:hover,
.btn:focus {
  background-color: #008080;
  color: #fff;
}

</style>