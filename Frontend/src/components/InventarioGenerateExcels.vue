<template>
  <div>
    <!-- http://ec2-34-247-57-206.eu-west-1.compute.amazonaws.com/uploadbalanza/ -->
    <el-row type="flex" justify="center">
      <el-col :span="12">
        <h1 style="padding-bottom:20px;"> Inventario </h1>
        <el-card v-if="input!=pass">
          <h5> Paso 1. Introduce la contraseña </h5>
          <el-input type="password" placeholder="Introduce la contraseña" v-model="input" show-password></el-input>
        </el-card>
        <el-card v-if="input===pass" v-loading=loading style="margin-top:20px">
          <h5> Paso 2. Generar ficheros de conteo de inventario desde dolibarr </h5>
          <el-button type="primary" @click="generateExcel"> Generar ficheros </el-button>
        </el-card>
      </el-col>
    </el-row>
    <el-row type="flex" justify="center" v-loading=loading2 style="padding-top:20px;">
      <el-col :span="12">
        <el-card v-if="input===pass">
          <h5> Paso 3. Generar reporte de cambio de stock</h5>
          <p> Para generar el reporte, sube el archivo "Product_list.xlsx"</p>
          <el-upload
            ref="upload"
            drag
            :action= url
            :on-preview="handlePreview"
            :file-list="fileList"
            :on-exceed="handleExceed"
            :on-error="handleError"
            :on-success="handleSuccess"
            limit=1
          >
            <i class="el-icon-upload"></i>
            <div class="el-upload__text">Suelta tu archivo csv aquí o <em>haz clic para cargar</em></div>
            <div slot="tip" class="el-upload__tip">Por favor, sube solamente archivos con extensión .xlsx</div>
          </el-upload>

          <el-button type="primary" :disabled="!showButtons || input!=pass" @click="downloadReport"> Descargar reporte </el-button>
        </el-card>
        <el-card v-if="showUpdateStock" v-loading=loading3 style="margin-top:20px;">
          <h5> Paso 4. Actualizar stock dolibarr</h5>
          <el-alert
            title="Atención, esta acción modificará los stocks de los productos de la base de datos de dolibarr por los stocks que hayas introducido en el fichero Product_list.xlsx que has subido en el paso 3. Antes de realizar esta acción, asegurate que has generado bien el reporte de stocks y que el fichero Product_list.xlsx. Una vez realizada esta acción, no podrás generar un fichero de reporte nuevo."
            type="warning"
            effect="dark">
          </el-alert>
          <el-button plain :disabled="!showButtons || input!=pass" @click="updateStock"> Actualizar stock en dolibarr </el-button>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import PedidosNPApi from '@/services/api/PedidosNP'
import InventarioApi from '@/services/api/Inventario'
export default {
  name: 'InventarioGenerateExcels',
  data () {
    return {
      input:'',
      fileList: [],
      pass: 'pod2019',
      attachments: [],
      showButtons: false,
      showUpdateStock: false,
      loading: false,
      loading2: false,
      loading3: false,
      url: process.env.API_URL + 'uploadInventory/',
      provider: {
        provider: ''
      }
      // rules: {
      //   provider: {required: true, message: 'Porfavor selecciona un Proveedor'}
      // },
    }
  },
  created () {
  },
  methods: {
    handleRemove (file, fileList) {
      return false
    },
    handlePreview (file) {
      console.log(file)
    },
    handleExceed (files, fileList) {
      this.$message.warning(`El límite de archivos es 1.`)
    },
    handleError (files, fileList) {
      this.$message.error(`Ha ocurrido un error. Por favor, vuelve a subir el archivo.`)
    },
    handleSuccess () {
      this.showButtons = true
    },
    generateExcel () {
      this.loading = true
      InventarioApi.generateExcel()
        .then(() => { this.loading = false })
    },
    downloadReport () {
      this.loading2 = true
      InventarioApi.downloadReport()
        .then(() => { 
          this.loading2 = false
          this.showUpdateStock = true
          })
      this.$refs.upload.clearFiles()
      
    },
    updateStock () {
      this.loading3 = true
      InventarioApi.updateStock()
        .then(() => { this.loading3 = false })
      this.$refs.upload.clearFiles()
    }
  }
}
</script>

<style scoped>
  h4 {
    font-weight: 700;
    color: hsl(0, 0%, 13%);
  }
  p {
    font-weight: 400;
    font-size: 14px;
    color: hsl(0, 0%, 45%);
  }
  button{
    margin-top: 20px;
  }
  .el-col{
    text-align: center;
  }
</style>