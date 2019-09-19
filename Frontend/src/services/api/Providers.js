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
  },
  addProvider (provider) {
    return new Promise((resolve, reject) => {
      axios.post('/providers/', provider)
        .then(function (response) {
          resolve(response)
        })
        .catch(function (error) {
          reject(error)
        })
    })
  },
  editProvider (provider) {
    return new Promise((resolve, reject) => {
      axios.put('/providers/', provider)
        .then(function (response) {
          resolve(response)
        })
        .catch(function (error) {
          reject(error)
        })
    })
  },
  deleteProvider (provider) {
    return new Promise((resolve, reject) => {
      axios.delete('/providers/', { params: { id: provider.id } })
        .then(function (response) {
          resolve(response)
        })
        .catch(function (error) {
          reject(error)
        })
    })
  }
}
