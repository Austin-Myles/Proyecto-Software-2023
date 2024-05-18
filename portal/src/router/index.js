import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AnalisisView from '../views/AnalisisView.vue'
import ServiceView from '../views/ServiceView.vue'
import ServiceRequestListView from '../views/ServiceRequestListView.vue'
import ServiceRequestView from '../views/ServiceRequestView.vue'
import InformationView from '../views/InformationView.vue'

import LoginView from '../views/LoginView.vue'
import ServiceSearchView from '../views/ServiceSearchView.vue'
import NotePage from '@/views/NotePageView.vue'
import { useUserStore } from '@/stores/user'
// TODO: error handling, session restriction, redirects,

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/home', redirect: '/' },
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/analisis',
      name: 'analisis',
      component: AnalisisView,
      beforeEnter: (to, from, next) => {
        const store = useUserStore()
        if (!store.user) {
          next({ name: 'login' })
        } else {
          next()
        }
      }
    },
    {
      path: '/service/:id',
      name: 'service',
      component: ServiceView
    },
    {
      path: '/service_request_list',
      name: 'service_request_list',
      component: ServiceRequestListView,
      beforeEnter: (to, from, next) => {
        const store = useUserStore()
        if (!store.user) {
          next({ name: 'login' })
        } else {
          next()
        }
      }
    },
    {
      path: '/service-request/:id',
      name: 'service-request',
      component: ServiceRequestView,
      props: true
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/search',
      name: 'search',
      component: ServiceSearchView
    },
    {
      path: '/notes/:id',
      name: 'NotePage',
      component: NotePage
    },
    {
      path: '/contact',
      name: 'ContactInfo',
      component: InformationView
    },
    {
      path: '/:pathMatch(.*)*',
      redirect: '/'
    }
  ]
})

export default router
