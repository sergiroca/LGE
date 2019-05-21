import Vue from 'vue'
import Router from 'vue-router'
import Basculas from '@/components/Basculas'
import PedidosFresco from '@/components/PedidosFresco'
import PedidosNP from '@/components/PedidosNP'
import Inventario from '@/components/Inventario'

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
    },
    {
      path: '/pedidos-np',
      name: 'PedidosNP',
      component: PedidosNP
    },
    {
      path: '/inventario',
      name: 'Inventario',
      component: Inventario
    }
  ],
  mode: 'history'
})
