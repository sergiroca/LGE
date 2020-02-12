// source of knowledge https://itnext.io/anyway-heres-how-to-do-ajax-api-calls-with-vue-js-e71e57d5cf12
import axios from 'axios'
import {cacheAdapterEnhancer} from 'axios-extensions'

export default {
  downloadBalanza () {
    return axios({
      url: '/downloadbalanza/',
      method: 'POST',
      responseType: 'blob', // important
      headers: {'Cache-Control': 'no-cache'},
      adapter: cacheAdapterEnhancer(axios.defaults.adapter, true)
    }).then((response) => {
      console.log(response)
      const url = window.URL.createObjectURL(new Blob([response.data]))
      console.log(url)
      const link = document.createElement('a')
      link.href = url
      link.setAttribute('download', 'Salida.zip') // or any other extension
      document.body.appendChild(link)
      link.click()
      link.parentNode.removeChild(link)
      console.log(link)
    })
  }
  // mapOffersFeatures (response) {
  //   const ProductOK = response.Products
  //
  //   return ProductOK
  // }
}
