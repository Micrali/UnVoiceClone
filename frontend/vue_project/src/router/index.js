import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../components/HomeView.vue'
import DashboardView from '../components/DashboardView.vue'

const routes = [
  { path: '/', component: HomeView },
  { path: '/dashboard', component: DashboardView }
]

export default createRouter({ history: createWebHistory(), routes })
