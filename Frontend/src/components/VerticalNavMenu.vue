<template>
  <div>
  <!--<el-radio-group v-model="isCollapse" style="margin-bottom: 20px;" size="mini">
    <el-radio-button :label="false">+</el-radio-button>
    <el-radio-button :label="true">-</el-radio-button>
  </el-radio-group> -->
  <el-row>
    <el-col>
      <div class="grid-content sidebar-brand">
        <img src="@/assets/lge.svg" width="70" height="70" alt="">
        <a href="#">La Garbancita Eco</a>
      </div>
      <div class="grid-content sidebar-brand powered">
        <a href="https://plantondemand.com">Powered by <span class="m-1"></span><img src="@/assets/favicon.png" width="15" height="15" alt=""> pod</a>
      </div>
    </el-col>
  </el-row>
  <el-menu :router="true" :default-active="activeLink" background-color="transparent" text-color="#D3D3D3" active-text-color="#fff"  @open="handleOpen" @close="handleClose" :collapse="isCollapse">
    <el-menu-item index="Basculas" >
      <i class="el-icon-goods iconWhite"></i>
      <span slot="title">Balanzas</span>
    </el-menu-item>
    <el-menu-item index="pedidos-fresco" >
      <i class="el-icon-goods iconWhite"></i>
      <span slot="title">Pedidos Fresco</span>
    </el-menu-item>
    <el-menu-item index="pedidos-np" >
      <i class="el-icon-goods iconWhite"></i>
      <span slot="title">No perecederos</span>
    </el-menu-item>
  </el-menu>
  </div>
</template>

<script>
export default {
  name: 'VerticalNavMenu',
  data () {
    return {
      activeIndex: '1',
      isCollapse: false
    }
  },
  methods: {
    handleOpen (key, keyPath) {
      console.log(key, keyPath)
    },
    handleClose (key, keyPath) {
      console.log(key, keyPath)
    }
  }
}

</script>

<style scoped>

</style>
