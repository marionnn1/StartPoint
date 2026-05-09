import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Ranking from '../views/Ranking.vue' // <-- Importar la nueva vista

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/ranking',
      name: 'ranking',
      component: Ranking // <-- Cambiar el componente aquí
    },
    // ... el resto de rutas (ligas, perfil)
  ]
})

export default router