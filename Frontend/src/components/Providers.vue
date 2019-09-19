<template>
  <div>
    <el-container class="height-100">
      <el-aside width="200px" class="bg-gradient">
        <VerticalNavMenu/>
      </el-aside>
      <el-container>
        <el-header v-if="input!=pass">
          <el-row type="flex" justify="center" style="margin-top:5%;">
            <el-col :span="12">
              <h1 style="padding-bottom:20px; text-align:center;"> Proveedores </h1>
              <el-card >
                <h5>Introduce la contraseña </h5>
                <el-input type="password" placeholder="Introduce la contraseña" v-model="input" show-password></el-input>
              </el-card>
            </el-col>
          </el-row>
        </el-header>


        <div v-if="input===pass">
          <el-header>
            <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
              <el-menu-item index="1">Proveedores no perecederos</el-menu-item>
              <el-menu-item index="2">Proveedores Fresco 1</el-menu-item>
              <el-menu-item index="3">Proveedores Fresco 2</el-menu-item>
            </el-menu>
          </el-header>
          <el-main>
            <el-row :gutter="20" style="margin-bottom: 20px">
              <el-button v-if="!add" type="primary" @click="toggleAdd">Crear nuevo Proveedor</el-button>
              <ProvidersAdd v-if ="add" @cancel="toggleAdd" @save="addProvider"/>
            </el-row>
            <el-row :gutter="20">
              <el-col :span="24">
                <!-- Filtered table by no perecedero -->
                <ProvidersTable v-if="activeIndex==='1'"
                                :tableData="providers | np "
                                :key="reloadKey"
                                @save="editProvider"
                                @delete="deleteProvider">
                </ProvidersTable>
                <!-- Filtered table by fresco 1 -->
                <ProvidersTable v-if="activeIndex==='2'"
                                :tableData="providers | fresco1 "
                                :key="reloadKey"
                                @save="editProvider"
                                @delete="deleteProvider">
                </ProvidersTable>
                <!-- Filtered table by fresco 2 -->
                <ProvidersTable v-if="activeIndex==='3'"
                                :tableData="providers | fresco2"
                                :key="reloadKey"
                                @save="editProvider"
                                @delete="deleteProvider">
                </ProvidersTable>
              </el-col>
            </el-row>
          </el-main>
        </div>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import VerticalNavMenu from '@/components/VerticalNavMenu'
import ProvidersApi from '@/services/api/Providers'
import ProvidersTable from '@/components/ProvidersTable'
import ProvidersAdd from '@/components/ProvidersAdd'
export default {
  name: 'Providers',
  components: {
    VerticalNavMenu,
    ProvidersTable,
    ProvidersAdd
  },
  data () {
    return {
      providers: [],
      providersFRESCOS1: [],
      providersFRESCOS2: [],
      providersNP: [],
      add: false,
      activeIndex: '1',
      reloadKey: 0,
      input: '',
      pass: 'pod2019'
    }
  },
  filters: {
    np: function (providers) {
      return providers.filter(provider => provider.group === 0)
    },
    fresco1: function (providers) {
      return providers.filter(provider => provider.group === 1)
    },
    fresco2: function (providers) {
      return providers.filter(provider => provider.group === 2)
    }
  },
  methods: {
    handleEditRow (index) {
      this.providers[index].edited = true
    },
    handleSaveRow (index) {
      this.providers[index].edited = false
    },
    editProvider (provider) {
      ProvidersApi.editProvider(provider)
        .then(() => {
          this.getProviders()
          this.$message({
            message: 'Proveedor editado.',
            type: 'success'
          })
        })
        .catch(() => {
          this.$message({
            message: 'Error editando el proveedor',
            type: 'error'
          })
        })
    },
    deleteProvider (provider) {
      this.$confirm('Esto eliminará el proveedor. Continuar?', 'Warning', {
        confirmButtonText: 'Eliminar',
        cancelButtonText: 'Cancelar',
        type: 'warning'
      }).then(() => {
        ProvidersApi.deleteProvider(provider)
          .then(() => {
            this.getProviders()
            this.$message({
              message: 'Proveedor eliminado',
              type: 'success'
            })
          })
          .catch(() => {
            this.$message({
              message: 'No se ha podido eliminar el proveedor',
              type: 'error'
            })
          })
      })
    },
    addProvider (provider) {
      ProvidersApi.addProvider(provider)
        .then(() => {
          this.toggleAdd()
          this.$message({
            message: 'Proveedor añadido correctamente.',
            type: 'success'
          })
          this.getProviders()
        })
        .catch(() => {
          this.$message({
            message: 'Error añadiendo el proveedor',
            type: 'error'
          })
          this.toggleAdd()
        })
    },
    toggleAdd () {
      this.add = !this.add
    },
    getProviders () {
      ProvidersApi.getProviders()
        .then((response) => {
          this.providers = response.data.Providers
          for (let i = 0; i < this.providers.length; i++) {
            this.$set(this.providers[i], 'edited', false) // ensure reactivity on vue object property
            // this.providers[i].edited = false // the "edited" property won't be reactive.
          }
          this.providers = this.providers.sort(function (a, b) {
            return a.name.localeCompare(b.name)
          })
        })
    },
    handleSelect (key, keyPath) {
      this.activeIndex = key
    }
  },
  created () {
    this.getProviders()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
