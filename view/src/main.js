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


import '@fortawesome/fontawesome-free/css/all.css'
import '@fortawesome/fontawesome-free/js/all.js'

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
    }
    
  ]
})

new Vue({ // eslint-disable-line no-new
  el: '#app',
  router,
  render: h => h(App)
})