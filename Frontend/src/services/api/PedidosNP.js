import axios from 'axios'
import {cacheAdapterEnhancer} from 'axios-extensions'

export default {
  downloadPedidoNP (provider) {
    return axios({
      url: '/download_pedidosNP/' + provider,
      method: 'GET',
      responseType: 'blob', // important
      headers: {'Cache-Control': 'no-cache'},
      adapter: cacheAdapterEnhancer(axios.defaults.adapter, true)
    }).then((response) => {
      const url = window.URL.createObjectURL(new Blob([response.data]))
      const link = document.createElement('a')
      link.href = url
      link.setAttribute('download', provider + '.xlsx') // or any other extension
      document.body.appendChild(link)
      link.click()
      link.parentNode.removeChild(link)
    })
  },
  deleteFilesNP () {
    return new Promise((resolve, reject) => {
      axios.get('/deleteFilesNP/')
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
