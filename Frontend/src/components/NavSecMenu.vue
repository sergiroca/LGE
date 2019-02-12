<template>
  <div>
  <h2 style="font-weight:bold"> Apartado de ventas</h2>
  <el-menu default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
    <el-menu-item index="1" @click="onWindow(0)">Clientes</el-menu-item>
    <el-menu-item index="2" @click="onWindow(1)">Ofertas</el-menu-item>
    <el-menu-item index="3" @click="onWindow(2)">Grupos Clientes</el-menu-item>
    <el-menu-item index="4" class="orders" @click="onWindow(3)">Pedidos</el-menu-item>
    <el-menu-item index="5" class="orders" @click="onWindow(4)">Procesar pedidos</el-menu-item>
  </el-menu>
  </div>
</template>

<script>
export default {
  name: 'NavSecMenu',
  data () {
    return {
      activeIndex: '1',
      isCollapse: false
    }
  },
  methods: {
    handleSelect (key, keyPath) {
      console.log(key, keyPath)
      // this.activeIndex = key
      // document.getElementsByClassName('is-active')[0].style = 'border-bottom-color: transparent;'
      // document.getElementsByClassName('is-active')[0].className = 'el-menu-item'
    },
    onWindow (N) {
      const payload = {
        window: N
      }
      this.$emit('onWindow', {payload})
    }
    // onOffers (evt) {
    //   const payload = {
    //     window: 1
    //   }
    //   this.$emit('onOffers', {payload})
    // }
  }
}
</script>

<style scoped>

</style>
