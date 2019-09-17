<template>
  <div>
    <el-row type="flex" justify="center" :key="rerender">
      <el-col :span="12">
        <h4> Pedidos Fresco 1 y 2</h4>
        <p> 1. Indica que pedido quieres hacer</p>
        <el-radio v-model="type" label="1" border>Viernes (pedido)</el-radio>
        <el-radio v-model="type" label="2" border>Lunes (ampliación)</el-radio>
        <div v-if="type !== ''">
          <div v-if="type === '1'">
            <p>
              2. Sube el archivo "datos_para_balanza.csv" <br>
              3. Sube el archivo de venta online "Productos_por_proveedor_online.csv" <br>
              4. Sube el archivo de venta física "Productos_por_proveedor_tienda.csv"
            </p>
            <el-upload
              class="upload-demo"
              drag
              :action= url
              :on-preview="handlePreview"
              :on-remove="handleRemove"
              :data="{type}"
              :limit="3"
              :on-exceed="handleExceed"
              :on-error="handleError"
              multiple
            >
              <i class="el-icon-upload"></i>
              <div class="el-upload__text">Suelta tus archivos csv aquí o <em>haz clic para cargar</em></div>
            </el-upload>
          </div>
          <div v-if="type === '2'">
            <p>
              2. Sube el archivo "datos_para_balanza.csv" <br>
              3. Sube el archivo de venta online "Productos_por_proveedor_online.csv" <br>
              4. Sube los archivos excel del pedido del viernes (FRESCO_1.xlsx y FRESCO_2.xlsx)
            </p>
            <el-upload
              drag
              :action= url
              :on-preview="handlePreview"
              :on-remove="handleRemove"
              :data="type"
              :limit="5"
              :on-exceed="handleExceed"
              :on-error="handleError"
              multiple
            >
              <i class="el-icon-upload"></i>
              <div class="el-upload__text">Suelta tus archivos csv aquí o <em>haz clic para cargar</em></div>
            </el-upload>
          </div>
          <el-button type="primary" @click="download">Convertir y descargar</el-button>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import PedidosApi from '@/services/api/PedidosFresco'
export default {
  name: 'addPedidosFresco',

  data () {
    return {
      type: '',
      attachments: [],
      url: process.env.API_URL + 'upload_pedidos_fresco/',
      rerender: 0
    }
  },
  methods: {
    addAttachment (file, fileList) {
      this.attachments.push(file)
      // http://localhost:5000/upload_pedidos_fresco/
    },
    handleRemove (file, fileList) {
      console.log(file, fileList)
    },
    handlePreview (file) {
      console.log(file)
    },
    handleExceed (files, fileList) {
      this.$message.warning(`El límite de archivos es 4. Si deseas modificarlo, borra el archivo anterior.`)
    },
    handleError (files, fileList) {
      this.$message.error(`Ha ocurrido un error. Por favor, vuelve a subir el archivo.`)
    },
    download () {
      const payload = {
        type: this.type
      }
      console.log(this)
      PedidosApi.uploadTypeFresco(payload)
        .then(this.forceRerender)
        .catch(error => alert(error.message))
      // PedidosApi.downloadFresco()
    },
    forceRerender () {
      this.rerender += 1
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
    margin-top: 40px;
    margin-bottom: 10px;
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
