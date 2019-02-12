<template>
  <div>
    <!-- http://ec2-34-247-57-206.eu-west-1.compute.amazonaws.com/uploadbalanza/ -->
    <el-row type="flex" justify="center">
      <el-col :span="12">
        <h4> Conversor Balanzas</h4>
        <p> Por favor, sube el archivo "Datos_para_balanza.csv" </p>
        <el-upload
          class="upload-demo"
          drag
          :action= url
          :on-preview="handlePreview"
          :on-remove="handleRemove"
          :file-list="fileList"
          :limit="1"
          :on-exceed="handleExceed"
          :on-error="handleError"
          >
          <i class="el-icon-upload"></i>
          <div class="el-upload__text">Suelta tu archivo csv aquí o <em>haz clic para cargar</em></div>
          <div slot="tip" class="el-upload__tip">Por favor, sube solamente archivos con extensión .csv</div>
        </el-upload>
        <el-button type="primary" @click="download">Descargar</el-button>
      </el-col>
    </el-row>

  </div>
</template>

<script>
import BalanzasApi from '@/services/api/Balanzas'
export default {
  name: 'addBasculas',
  data () {
    return {
      attachments: [],
      url: process.env.API_URL + 'uploadbalanza/'
    }
  },
  methods: {
    handleRemove (file, fileList) {
      console.log(file, fileList)
    },
    handlePreview (file) {
      console.log(file)
    },
    handleExceed (files, fileList) {
      this.$message.warning(`El límite de archivos es 1. Si deseas modificarlo, borra el archivo anterior.`)
    },
    handleError (files, fileList) {
      this.$message.error(`Ha ocurrido un error. Por favor, vuelve a subir el archivo.`)
    },
    download () {
      BalanzasApi.downloadBalanza()
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
