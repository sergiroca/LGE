<template>
  <div>
    <h2 style="font-weight:bold"> Apartado de compras</h2>
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
      <el-menu-item index="1">Proveedores</el-menu-item>
      <el-menu-item index="2">Albaranes</el-menu-item>
    </el-menu>
  </div>
</template>

<script>
export default {
  name: 'NavSecMenuPurchases',
  data () {
    return {
      activeIndex: '1',
      isCollapse: false
    }
  },
  methods: {
    handleSelect (key, keyPath) {
      console.log(key, keyPath)
    }
  }
}
</script>

<style scoped>

</style>
