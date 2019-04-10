import axios from 'axios'

export default {
  downloadPedidoNP (provider) {
    return axios({
      url: '/download_pedidosNP/' + provider,
      method: 'GET',
      responseType: 'blob' // important
    }).then((response) => {
      console.log(response)
      const url = window.URL.createObjectURL(new Blob([response.data]))
      console.log(url)
      const link = document.createElement('a')
      link.href = url
      link.setAttribute('download', 'Pedidos_no_perecederos.xlsx') // or any other extension
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
