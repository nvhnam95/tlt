import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import VueSidebarMenu from 'vue-sidebar-menu'
import 'vue-sidebar-menu/dist/vue-sidebar-menu.css'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import Home from './components/Home.vue'
import PO from './components/PO.vue'
import NhapKho from './components/NhapKho.vue'
import XuatKho from './components/XuatKho.vue'
import XuatNhapTon from './components/XuatNhapTon.vue'

import '@fortawesome/fontawesome-free/css/all.css'
import '@fortawesome/fontawesome-free/js/all.js'

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(VueRouter)
Vue.use(VueSidebarMenu)

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
    }
  ]
})

new Vue({ // eslint-disable-line no-new
  el: '#app',
  router,
  render: h => h(App)
})