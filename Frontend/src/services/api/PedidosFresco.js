// source of knowledge https://itnext.io/anyway-heres-how-to-do-ajax-api-calls-with-vue-js-e71e57d5cf12
import axios from 'axios'
import { cacheAdapterEnhancer } from 'axios-extensions'
export default {
  uploadTypeFresco (payload) {
    return axios({
      url: '/upload_type_fresco/',
      method: 'POST',
      data: payload,
      responseType: 'blob', // important
      headers: {'Cache-Control': 'no-cache'},
      adapter: cacheAdapterEnhancer(axios.defaults.adapter, true)
    }).then((response) => {
      console.log(response)
      const url = window.URL.createObjectURL(new Blob([response.data]))
      console.log(url)
      const link = document.createElement('a')
      link.href = url
      link.setAttribute('download', 'Pedidos_Fresco.zip') // or any other extension
      document.body.appendChild(link)
      link.click()
      link.parentNode.removeChild(link)
      console.log(link)
    })
  }
}
// export default {
//   uploadTypeFresco (payload) {
//     const path = 'http://0.0.0.0:5000/upload_type_fresco/'
//     axios.post(path, payload)
//     return axios({
//       url: '/download_pedidos_fresco/',
//       method: 'GET',
//       responseType: 'blob' // important
//     }).then((response) => {
//       console.log(response)
//       const url = window.URL.createObjectURL(new Blob([response.data]))
//       console.log(url)
//       const link = document.createElement('a')
//       link.href = url
//       link.setAttribute('download', 'Pedidos_Fresco.zip') // or any other extension
//       document.body.appendChild(link)
//       link.click()
//       link.parentNode.removeChild(link)
//       console.log(link)
//     })
//   }
// }
