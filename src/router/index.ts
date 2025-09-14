import {getRouter} from "@/globaltechia/utils.ts";
import ActivationsReport from "@/views/ActivationsReport.vue";
import LocalLoginView from "@/views/LocalLoginView.vue";
import LocalDashboarView from "@/views/LocalDashboardView.vue";
import UserView from "@/globaltechia/views/UserView.vue";
import UserViewList from "@/globaltechia/views/UserViewList.vue";

const local_routes = [
  {
    path: '/:app/User/list',
    name: 'list_user',
    component: UserViewList,
  },
  {
    path: '/:app/User',
    name: 'create_user',
    component: UserView,
  },
  {
    path: '/:app/User/:id',
    name: 'edit_user',
    component: UserView,
  },
  {
    path: '/:app/reporte_activaciones',
    name: 'reporte_activaciones',
    component: ActivationsReport,
  }
];

const router = getRouter(local_routes,LocalLoginView,LocalDashboarView);

export default router
