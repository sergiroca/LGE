// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import App from './App'
import router from './router'
import axios from 'axios'
import BootstrapVue from 'bootstrap-vue'
import locale from 'element-ui/lib/locale/lang/es'

Vue.use(BootstrapVue)

Vue.use(ElementUI, { locale })
axios.defaults.baseURL = process.env.API_URL // 'http://ec2-34-247-57-206.eu-west-1.compute.amazonaws.com/'
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
