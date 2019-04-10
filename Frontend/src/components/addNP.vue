<template>
  <div>
    <!-- http://ec2-34-247-57-206.eu-west-1.compute.amazonaws.com/uploadbalanza/ -->
    <el-row type="flex" justify="center">
      <el-col :span="12">
        <h4> Pedidos No Perecederos</h4>
        <p> Por favor, añade los archivos:</p>
        <p> "Products_Stocks.csv"</p>
        <p> "sales_physical_3months_prior.csv"</p>
        <p> "sales_physical_3months_after.csv"</p>
        <p> "sales_online_3months_prior.csv"</p>
        <p> "sales_online_3months_after.csv"</p>
        <p> "sales_physical_12months.csv"</p>
        <p> "sales_online_12months.csv"</p>
        <el-upload
          class="upload-demo"
          drag
          :action= url
          :on-preview="handlePreview"
          :on-remove="handleRemove"
          :file-list="fileList"
          :limit="7"
          multiple
          :on-exceed="handleExceed"
          :on-error="handleError"
        >
          <i class="el-icon-upload"></i>
          <div class="el-upload__text">Suelta tu archivo csv aquí o <em>haz clic para cargar</em></div>
          <div slot="tip" class="el-upload__tip">Por favor, sube solamente archivos con extensión .csv</div>
        </el-upload>
        <el-row>
          <br>
          <br>
          <p>Escoge el Proveedor</p>
          <el-form :model="provider" ref="providerForm" :rules="rules">
            <el-col>
              <el-form-item prop="provider">
                <el-select v-model="provider.provider" filterable placeholder="Proveedor">
                  <el-option
                    v-for="item in providers"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                  </el-option>
                </el-select>
              </el-form-item>
            </el-col>
            <el-col>
              <el-form-item>
                <el-button type="primary" :disabled="provider.provider === ''" @click="download('providerForm')">Descargar</el-button>
              </el-form-item>
            </el-col>
          </el-form>
        </el-row>
      </el-col>
    </el-row>

  </div>
</template>

<script>
import PedidosNPApi from '@/services/api/PedidosNP'
export default {
  name: 'addNP',
  data () {
    return {
      attachments: [],
      url: process.env.API_URL + 'uploadPedidosNP/',
      provider: {
        provider: ''
      },
      rules: {
        provider: {required: true, message: 'Porfavor selecciona un Proveedor'}
      },
      providers: [
        {
          value: 'segura',
          label: 'El rincón del segura'
        },
        {
          value: 'gumendi',
          label: 'gumendi'
        }]
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
      this.$message.warning(`El límite de archivos es 7. Si deseas modificarlo, borra el archivo anterior.`)
    },
    handleError (files, fileList) {
      this.$message.error(`Ha ocurrido un error. Por favor, vuelve a subir el archivo.`)
    },
    download (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          PedidosNPApi.downloadPedidoNP(this.provider.provider)
        } else {
          console.log('error submit!!')
          return false
        }
      })
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
