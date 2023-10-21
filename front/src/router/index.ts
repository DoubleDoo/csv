import { createRouter, createWebHistory } from 'vue-router'
import LoginPage from '../views/LoginPage.vue'
import HomePage from '../views/HomePage.vue'
import FileGrid from '../components/FileGrid.vue'
import FileTable from '../components/FileTable.vue'
import { useUserStore } from '@/stores/user'
import { useFileStore } from '@/stores/file'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      name: 'login',
      component: LoginPage,
      async beforeEnter(to, from, next) {
        // const file = useFileStore();
        // await file.requestFiles();
        const user = useUserStore()
        if (user.isAuthenticated) {
          next('/')
        }
        next()
      },
    },
    {
      path: '/',
      name: 'Home',
      component: HomePage,
      children: [
        {
          name: 'AllFiles',
          path: '',
          component: FileGrid,
        },
        {
          name: 'File',
          path: ':fileUUID',
          component: FileTable,
        },
      ],
      async beforeEnter(to, from, next) {
        const file = useFileStore()
        await file.requestFiles()
        const user = useUserStore()
        if (!user.isAuthenticated) {
          next('/login')
        }
        next()
      },
    },
  ],
})

export default router
