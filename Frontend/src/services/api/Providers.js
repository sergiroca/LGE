import axios from 'axios'
export default {
  getProviders () {
    return new Promise((resolve, reject) => {
      axios.get('/providers/')
        .then(function (response) {
          resolve(response)
        })
        .catch(function (error) {
          reject(error)
        })
    })
  }
}