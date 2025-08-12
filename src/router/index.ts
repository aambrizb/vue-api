import { createRouter, createWebHistory } from 'vue-router'
import GenericModelView from "@/globaltechia/components/GenericModelView.vue";
import GenericList from "@/globaltechia/components/GenericList.vue";
import LoginView from "@/globaltechia/views/LoginView.vue";
import SystemView from "@/globaltechia/views/SystemView.vue";
import ActivationsReport from "@/views/ActivationsReport.vue";
function isAuthenticated() {
  return !!localStorage.getItem('token')
}

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: () => (isAuthenticated() ? '/view' : '/login')
    },
    {
      path: '/:pathMatch(.*)*',
      redirect: '/'
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView,
    },
    {
      path: '/view',
      component: SystemView,
      children:[
        {
          path: ':app/:view',
          name: 'create',
          component: GenericModelView,
        },
        {
          path: ':app/:view/:id',
          name: 'edit',
          component: GenericModelView,
        },
        {
          path: ':app/:view/list',
          name: 'list',
          component: GenericList,
        },
        {
          path: ':app/:view/reporte_activaciones',
          name: 'reporte_activaciones',
          component: ActivationsReport,
        }
      ]
    }
  ],
})

router.beforeEach((to, from, next) => {
  if (to.name != 'login' && !isAuthenticated()) {
    return next('/login')
  }

  next()

})


export default router
