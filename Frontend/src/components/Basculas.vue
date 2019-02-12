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
          <addBasculas/>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import VerticalNavMenu from '@/components/VerticalNavMenu'
import addBasculas from '@/components/addBasculas'
export default {
  name: 'Basculas',
  components: {
    VerticalNavMenu,
    addBasculas
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
