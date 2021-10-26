import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import VueSidebarMenu from 'vue-sidebar-menu'
import 'vue-sidebar-menu/dist/vue-sidebar-menu.css'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import './assets/css/main.css';
import TrendChart from "vue-trend-chart";

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import Home from './components/Home.vue'
import PO from './components/PO.vue'
import NhapKho from './components/NhapKho.vue'
import XuatKho from './components/XuatKho.vue'
import XuatNhapTon from './components/XuatNhapTon.vue'

import ChiPhiBanHang from './components/chi_phi/ChiPhiBanHang.vue'
import ChiPhiQuanLy from './components/chi_phi/ChiPhiQuanLy.vue'
import ChiPhiKhac from './components/chi_phi/ChiPhiKhac.vue'
import ThucTeChi from './components/chi_phi/ThucTeChi.vue'
import DoanhThuBosch from './components/chi_phi/DoanhThuBosch.vue'
import DoanhThungoai from './components/chi_phi/DoanhThuNgoai.vue'
import KetQuaKinhDoanh from './components/chi_phi/KetQuaKinhDoanh.vue'
import Login from './components/Login.vue'
import Customer from './components/Customer.vue'
import CongNo from './components/cong_no/CongNo.vue'
import User from './components/User.vue'
import TaiKhoan from './components/TaiKhoan.vue'


import '@fortawesome/fontawesome-free/css/all.css'
import '@fortawesome/fontawesome-free/js/all.js'
// import axios from "axios";

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(VueRouter)
Vue.use(VueSidebarMenu)
Vue.use(TrendChart);

const router = new VueRouter({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/po',
      name: 'PO',
      component: PO
    },
    {
      path: '/nhap-kho',
      name: 'NhapKho',
      component: NhapKho
    },
    {
      path: '/xuat-kho',
      name: 'Xuất Kho',
      component: XuatKho
    },
    {
      path: '/xuat-nhap-ton',
      name: 'Xuất-Nhập-Tồn',
      component: XuatNhapTon
    },
    {
      path: '/chi-phi-ban-hang',
      name: 'Chi Phí Bán Hàng',
      component: ChiPhiBanHang
    },
    {
      path: '/chi-phi-quan-ly',
      name: 'Chi Phí Quản Lý',
      component: ChiPhiQuanLy
    },
    {
      path: '/chi-phi-khac',
      name: 'Chi Phí Khác',
      component: ChiPhiKhac
    },
    {
      path: '/thuc-te-chi',
      name: 'Thực Tế Chi',
      component: ThucTeChi
    },
    {
      path: '/doanh-thu-bosch',
      name: 'Doanh Thu Bosch',
      component: DoanhThuBosch
    },
    {
      path: '/doanh-thu-ngoai',
      name: 'Doanh Thu Ngoai',
      component: DoanhThungoai
    },
    {
      path: '/ket-qua-kinh-doanh',
      name: 'Kết Quả Kinh Doanh',
      component: KetQuaKinhDoanh
    },    
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/cong-no',
      name: 'CongNo',
      component: CongNo
    },
    {
      path: '/customer',
      name: 'Customer',
      component: Customer
    },
    {
      path: '/user',
      name: 'User',
      component: User
    },
    {
      path: '/tai-khoan',
      name: 'TaiKhoan',
      component: TaiKhoan
    }
  ]
})

// let current_user = {}

// let auth_url = process.env.VUE_APP_API_ENDPOINT + "/api/v1/current-user"

router.beforeEach((to, from, next) => {
  let is_authenticated = localStorage.getItem("is_authenticated")
  // let token = localStorage.getItem("token")
  // axios.get(auth_url, headers= {'Authentication': "Bearer " + token}).then((response) => {
  //   console.log(response.data)
  // })

  if (to.name !== 'Login' && !is_authenticated) next({ name: 'Login' })
  else next()

})
new Vue({ // eslint-disable-line no-new
  el: '#app',
  router,
  render: h => h(App)
})
