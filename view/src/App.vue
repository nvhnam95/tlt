<template>
  <div id="demo" :class="[{ collapsed: collapsed }, { onmobile: isOnMobile }]">
    <div class="demo">
      <div class="container">
        <router-view />
      </div>
      <sidebar-menu
        :menu="menu"
        :collapsed="collapsed"
        :show-one-child="true"
        @toggle-collapse="onToggleCollapse"
        :width="'200px'"
        @item-click="onItemClick"
      />
      <div
        v-if="isOnMobile && !collapsed"
        class="sidebar-overlay"
        @click="collapsed = true"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "App",
  data() {
    return {
      full_menu_paths: [
        {
          href: "/",
          title: "Home",
          icon: "fa fa-home",
          permission: "",
        },
        {
          title: "Quản Lý Kho",
          icon: "fa fa-archive",
          child: [
            {
              href: "/po",
              title: "PO",
              icon: "fa fa-shopping-cart",
              permission: "can_view_po",
            },
            {
              href: "/nhap-kho",
              title: "Nhập Kho",
              icon: "fa fa-download",
              permission: "can_view_nhap_kho",
            },
            {
              href: "/xuat-kho",
              title: "Xuất Kho",
              icon: "fa fa-upload",
              permission: "can_view_xuat_kho",
            },
            {
              href: "/xuat-nhap-ton",
              title: "Xuất-Nhập-Tồn",
              icon: "fa fa-table",
              permission: "can_view_xnt",
            },
          ],
        },
        {
          title: "Quản Lý Chi Phí",
          icon: "fa fa-wallet",
          child: [
            {
              href: "/chi-phi-ban-hang",
              title: "Chi phí bán hàng",
              icon: "fa fa-sign-out-alt",
              permission: "can_view_chi_phi_ban_hang",
            },
            {
              href: "chi-phi-quan-ly",
              title: "Chi phí quản lý",
              icon: "fa fa-user-friends",
              permission: "can_view_chi_phi_quan_ly",
            },
            {
              href: "chi-phi-khac",
              title: "Chi phí khác",
              icon: "fa fa-ellipsis-h",
              permission: "can_view_chi_phi_khac",
            },
            {
              href: "thuc-te-chi",
              title: "Thực tế chi",
              icon: "fa fa-comment-dollar",
              permission: "can_view_thuc_te_chi",
            },
            {
              href: "doanh-thu-bosch",
              title: "Doanh thu Bosch",
              icon: "fa fa-bold",
              permission: "can_view_doanh_thu_bosch",
            },
            {
              href: "doanh-thu-ngoai",
              title: "Doanh thu ngoài",
              icon: "fa fa-mail-bulk",
              permission: "can_view_doanh_thu_ngoai",
            },
            {
              href: "ket-qua-kinh-doanh",
              title: "Kết quả kinh doanh",
              icon: "fa fa-file-contract",
              permission: "can_view_ket_qua_kinh_doanh",
            },
          ],
        },
        {
          title: "Công Nợ",
          icon: "fa fa-credit-card",
          href: "/cong-no",
          permission: "can_view_cong_no",
        },
        {
          title: "Quản Lý Chung",
          icon: "fa fa-cogs",
          child: [
            {
              href: "/customer",
              title: "Khách Hàng",
              icon: "fa fa-handshake",
              permission: "can_view_khach_hang",
            },
            {
              href: "/user",
              title: "Người Dùng",
              icon: "fa fa-user-cog",
              permission: "can_view_user",
            },
          ],
        },
      ],
      menu: [
        {
          header: "Menu",
          hiddenOnCollapse: true,
        },
      ],
      isOnMobile: false,
      collapsed: true,
      permissions: [],
    };
  },
  async mounted() {
    // let token = localStorage.getItem("token");
    let token = document.cookie
    if (token.includes("Token"))
      token = token.split(";")[0].split("=")[1]

    if (token)
      axios.defaults.headers.common["Authorization"] = "Token " + token;
    await this.get_permissions();

    this.onResize();
    window.addEventListener("resize", this.onResize);
    document.title = "Quản lý";

    this.render_menu();
  },
  methods: {
    async get_permissions() {
      let url = new URL(
        process.env.VUE_APP_API_ENDPOINT + "/api/v1/current-user"
      );

      await axios({
        method: "get",
        url: url,
      })
        .then((response) => {
          this.permissions = response.data.permissions;
        })
        .catch(function () {
          document.cookie = "Token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
          this.$router.push("Login");
        });
    },
    render_menu() {
      for (let m of this.full_menu_paths) {
        // let cloned_menu = {"title": m.title, "icon": m.icon}
        if ("child" in m) {
          let cloned_child = [];
          for (let i of m.child) {
            if (this.permissions.includes(i.permission)) {
              cloned_child.push({ title: i.title, icon: i.icon, href: i.href });
            }
          }
          if (cloned_child.length > 0) {
            m.child = cloned_child;
            this.menu.push(m);
          }
        } else {
          if (this.permissions.includes(m.permission)) {
            this.menu.push(m);
          }
        }
      }
      this.menu.push({
            href: "/tai-khoan",
            title: "Tài Khoản",
            icon: "fa fa-sign-out-alt",
            permission: "",
          });
    },
    onToggleCollapse(collapsed) {
      this.collapsed = collapsed;
    },
    onItemClick() {},
    onResize() {
      if (window.innerWidth <= 767) {
        this.isOnMobile = true;
        this.collapsed = true;
      } else {
        this.isOnMobile = false;
        this.collapsed = false;
      }
    },
  },
};
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,600");

body,
html {
  margin: 0;
  padding: 0;
}

body {
  font-family: "Source Sans Pro", sans-serif;
  font-size: 18px;
  background-color: #f2f4f7;
  color: #262626;
}

#demo {
  padding-left: 190px;
  transition: 0.3s ease;
}
#demo.collapsed {
  padding-left: 65px;
}
#demo.onmobile {
  padding-left: 65px;
}

.sidebar-overlay {
  position: fixed;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  background-color: #000;
  opacity: 0.5;
  z-index: 900;
}

.demo {
  padding: 20px;
}

.container {
  max-width: 30000px !important;
}
</style>
