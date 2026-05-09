import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: Home },
    { path: '/ranking', component: Home }, // Temporalmente apuntan a Home
    { path: '/ligas', component: Home },
    { path: '/perfil', component: Home },
  ]
})

export default router