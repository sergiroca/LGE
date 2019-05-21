import axios from 'axios'
import { cacheAdapterEnhancer } from 'axios-extensions'
export default {
  generateExcel () {
    return axios({
      url: '/generateExcel/',
      method: 'GET',
      responseType: 'blob', // important
      headers: {'Cache-Control': 'no-cache'},
      adapter: cacheAdapterEnhancer(axios.defaults.adapter, true)
    }).then((response) => {
      console.log(response)
      const url = window.URL.createObjectURL(new Blob([response.data]))
      console.log(url)
      const link = document.createElement('a')
      link.href = url
      link.setAttribute('download', 'Inventario.zip') // or any other extension
      document.body.appendChild(link)
      link.click()
      link.parentNode.removeChild(link)
      console.log(link)
    })
  },
  downloadReport () {
    return axios({
      url: '/downloadReport/',
      method: 'GET',
      responseType: 'blob', // important
      headers: {'Cache-Control': 'no-cache'},
      adapter: cacheAdapterEnhancer(axios.defaults.adapter, true)
    }).then((response) => {
      console.log(response)
      const url = window.URL.createObjectURL(new Blob([response.data]))
      console.log(url)
      const link = document.createElement('a')
      link.href = url
      link.setAttribute('download', 'stock_reporte.xlsx') // or any other extension
      document.body.appendChild(link)
      link.click()
      link.parentNode.removeChild(link)
      console.log(link)
    })
  },
  updateStock () {
    return new Promise((resolve, reject) => {
      axios.get('/updateStock/')
        .then(function (response) {
          console.log(response)
          resolve(response)
        })
        .catch(function (error) {
          console.log(error)
          reject(error)
        })
    })
  }
}