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

      <b-form-group
        id="input-group-1"
        label="Mã Khách Hàng:"
        label-for="client_code"
      >
        <b-form-input
          id="client_code"
          v-model="form.client_code"
          type="text"
          list="customer-list"
        ></b-form-input>
        <datalist id="customer-list">
          <option v-for="code in customer_codes" v-bind:key="code">
            {{ code }}
          </option>
        </datalist>
      </b-form-group>

      <b-form-group id="product_code" label="Mã Hàng:" label-for="product_code">
        <b-form-input
          id="product_code"
          v-model="form.product_code"
          type="text"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Số Lượng:" label-for="quantity">
        <b-form-input
          id="quantity"
          v-model="form.quantity"
          type="text"
          v-on:input="update_thanh_tien"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-3" label="Giá Bán:" label-for="price">
        <b-form-input
          id="price"
          type="text"
          v-model="form.price"
          v-on:input="update_thanh_tien"
        ></b-form-input>
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
  mounted() {
    let url = process.env.VUE_APP_API_ENDPOINT + "/api/v1/customers";
    let component = this
    axios({
      method: "get",
      url: url,
    })
      .then((response) => {
        for (let c of response.data){
          component.customer_codes.push(c.code)

        }
      })
      .catch(function (error) {
        alert(error);
      });
  },
  data() {
    return {
      customer_codes: [],
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
    update_thanh_tien() {
      if (this.form.quantity && this.form.price)
        this.form.total = parseFloat(
          this.form.quantity * this.form.price
        ).toFixed(2);
    },
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