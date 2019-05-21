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
          <InventarioGenerateExcels/>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import VerticalNavMenu from '@/components/VerticalNavMenu'
import InventarioGenerateExcels from '@/components/InventarioGenerateExcels'
export default {
  name: 'Inventario',
  components: {
    VerticalNavMenu,
    InventarioGenerateExcels
  },
  methods: {
  },
  created () {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
