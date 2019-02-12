<template>
  <div>
    <el-container class="height-100">
      <el-aside width="200px" class="bg-gradient">
        <VerticalNavMenu/>
      </el-aside>
      <el-container>
        <el-header>
          <!-- <NavMenu/> -->
        </el-header>
        <el-main>
          <!-- <NavSecMenu/> -->
          <addPedidosFresco/>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import VerticalNavMenu from '@/components/VerticalNavMenu'
import addPedidosFresco from '@/components/addPedidosFresco'
// import NavMenu from '@/components/NavMenu'
// import NavSecMenuPurchases from '@/components/NavSecMenu'
export default {
  name: 'HelloWorld',
  components: {
    VerticalNavMenu,
    addPedidosFresco
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
