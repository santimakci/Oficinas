import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../components/Home'
import Office from '../components/Offices'
import Reserves from '../components/Reserves'
import createReserve from '../components/ReserveForm'


Vue.use(VueRouter)

const routes = [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/offices',
      name: 'Offices',
      component: Office
    },
    {
      path: '/office/:id',
      name: 'Reserves',
      component: Reserves
    },
    {
      path: '/newreserve/:id',
      name: 'createReserve',
      component: createReserve
    },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router