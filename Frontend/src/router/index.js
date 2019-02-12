import Vue from 'vue'
import Router from 'vue-router'
import Basculas from '@/components/Basculas'
import PedidosFresco from '@/components/PedidosFresco'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Basculas',
      component: Basculas
    },
    {
      path: '/basculas',
      name: 'Basculas',
      component: Basculas
    },
    {
      path: '/pedidos-fresco',
      name: 'PedidosFresco',
      component: PedidosFresco
    }
  ],
  mode: 'history'
})
