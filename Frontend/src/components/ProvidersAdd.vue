<template>
  <div>
    <el-row>
      <el-card>
        <h5>Añadir proveedor</h5>
        <el-form :inline="true" :model="provider" class="demo-form-inline" style="margin-top:20px;">
          <el-form-item label="Nombre">
            <el-input v-model="provider.name" placeholder="Nombre proveedor"></el-input>
          </el-form-item>
          <el-form-item label="Palabra clave">
            <el-input v-model="provider.keyword" placeholder="Palabra clave"></el-input>
          </el-form-item>
          <el-form-item label="Tipo">
            <el-select v-model="provider.group" placeholder="Tipo proveedor">
              <el-option label="No perecedero" value="0"></el-option>
              <el-option label="Fresco 1" value="1"></el-option>
              <el-option label="Fresco 2" value="2"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item>
            <el-button type="primary"
                       :loading=loading
                       @click="handleSave"
                       :disabled="(!provider.name || !provider.keyword || !provider.group)">
              Guardar
            </el-button>
            <el-button type="danger" @click="handleCancel" plain>Cancelar</el-button>
          </el-form-item>
        </el-form>
      </el-card>
    </el-row>

  </div>
</template>

<script>
export default {
  name: 'ProvidersAdd',
  components: {
  },
  props: [],
  data () {
    return {
      provider: {
        name: '',
        keyword: '',
        group: null
      },
      loading: false
    }
  },
  methods: {
    handleSave (index) {
      this.loading = true
      this.$emit('save', this.provider)
    },
    handleCancel () {
      this.$emit('cancel')
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
