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
          <el-row :gutter="20" style="margin-bottom: 20px">
            <el-button type="success" @click="showProductAddModal">Crear nuevo Proveedor</el-button>
          </el-row>
          <el-row :gutter="20">
            <el-col :span="8">
              <div class="grid-content bg-purple">
                <el-row>
                  <p>
                    Proveedores No Perecederos
                  </p>
                </el-row>
                <el-table
                  max-height="500"
                  :data="providersNP"
                  style="width: 100%">
                  <el-table-column
                    prop="name"
                    label="Nombre"
                    width="180">
                  </el-table-column>
                  <el-table-column
                    prop="keyword"
                    label="Keyword"
                    width="180">
                  </el-table-column>
                </el-table>              
              </div>
            </el-col>
            <el-col :span="8">
              <div class="grid-content bg-purple">
                <el-row>
                  <p>
                    Proveedores Frescos 1
                  </p>
                </el-row>
                <el-table
                  max-height="500"
                  :data="providersFRESCOS1"
                  style="width: 100%">
                  <el-table-column
                    prop="name"
                    label="Nombre"
                    width="180">
                  </el-table-column>
                  <el-table-column
                    prop="keyword"
                    label="Keyword"
                    width="180">
                  </el-table-column>
                </el-table>
              </div>
            </el-col>
            <el-col :span="8">
              <div class="grid-content bg-purple">
                <el-row>
                  <p>
                    Proveedores Frescos 2
                  </p>
                </el-row>
                <el-table
                  max-height="500"
                  :data="providersFRESCOS2"
                  style="width: 100%">
                  <el-table-column
                    prop="name"
                    label="Nombre"
                    width="180">
                  </el-table-column>
                  <el-table-column
                    prop="keyword"
                    label="Keyword"
                    width="180">
                  </el-table-column>
                </el-table>
              </div>
            </el-col>
          </el-row>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import VerticalNavMenu from '@/components/VerticalNavMenu'
import ProvidersApi from '@/services/api/Providers'
export default {
  name: 'Providers',
  components: {
    VerticalNavMenu
  },
  data () {
    return {
      providersFRESCOS1: [],
      providersFRESCOS2: [],
      providersNP: []
    }
  },
  methods: {
  },
  created () {
    ProvidersApi.getProviders()
      .then((response) => {
        let providers = response.data.Providers
        for (let i = 0; i < providers.length; i++) {
          console.log(providers[i])
          if (providers[i].group === 0) {
            this.providersNP.push(providers[i])
          } else if (providers[i].group === 1) {
            this.providersFRESCOS1.push(providers[i])
          } else if (providers[i].group === 2) {
            this.providersFRESCOS2.push(providers[i])
          }
        }
      })
  },
  methods: {
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
