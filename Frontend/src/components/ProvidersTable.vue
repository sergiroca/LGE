<template>
  <div>
    <el-table
            max-height="400"
            :data="tableData"
            style="width: 100%">
      <el-table-column
              prop="name"
              label="Nombre">
        <template slot-scope="scope">
          <span v-if="!scope.row.edited"> {{scope.row.name}}</span>
          <el-input v-if="scope.row.edited" v-model="scope.row.name" :disabled="!scope.row.edited"></el-input>
        </template>
      </el-table-column>
      <el-table-column
              prop="keyword"
              label="Keyword">
        <template slot-scope="scope">
          <span v-if="!scope.row.edited"> {{scope.row.keyword}}</span>
          <el-input v-if="scope.row.edited" v-model="scope.row.keyword" :disabled="!scope.row.edited"></el-input>
        </template>
      </el-table-column>
      <el-table-column align="right">
        <template slot-scope="scope">
          <el-button v-if="!scope.row.edited" type="default" size="mini" @click="handleEditRow(scope.$index)">Editar</el-button>
          <el-button v-if="!scope.row.edited" type="danger" size="mini" @click="handleDeleteRow(scope.$index)" plain>Eliminar</el-button>
          <el-button v-if="scope.row.edited" type="primary" size="mini" @click="handleSaveRow(scope.$index)">Guardar</el-button>
          <el-button v-if="scope.row.edited" type="default" size="mini" @click="handleCancelRow(scope.$index)">Cancelar</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: 'ProvidersTable',
  components: {
  },
  props: ['tableData'],
  data () {
    return {
    }
  },
  methods: {
    handleEditRow (index) {
      this.tableData[index].edited = true
    },
    handleSaveRow (index) {
      this.tableData[index].edited = false
      this.$emit('save', this.tableData[index])
    },
    handleCancelRow (index) {
      this.tableData[index].edited = false
    },
    handleDeleteRow (index) {
      this.tableData[index].edited = false
      this.$emit('delete', this.tableData[index])
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
