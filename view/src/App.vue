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
      @item-click="onItemClick" />
      <div v-if="isOnMobile && !collapsed" class="sidebar-overlay" @click="collapsed = true"/>
    </div>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      menu: [
        {
          header: "Menu",
          hiddenOnCollapse: true,
        },
        {
          href: "/",
          title: "Home",
          icon: "fa fa-home",
        },
        {
          href: "/po",
          title: "PO",
          icon: "fa fa-code",
        },
        {
          href: "/nhap-kho",
          title: "Nhập Kho",
          icon: "fa fa-cogs",
        },
        {
          href: "/xuat-kho",
          title: "Xuất Kho",
          icon: "fa fa-bell",
        },
        {
          href: "/xuat-nhap-ton",
          title: "Xuất-Nhập-Tồn",
          icon: "fa fa-palette",
        },
      ],
      isOnMobile: false,
      collapsed: false,
    };
  },
  mounted() {
    this.onResize();
    window.addEventListener("resize", this.onResize);
  },
  methods: {
    onToggleCollapse(collapsed) {
      console.log("onToggleCollapse");
      this.collapsed = collapsed
    },
    onItemClick() {
      console.log("onItemClick");
    },
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
  max-width: 900px;
}
</style>
