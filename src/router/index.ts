import {getRouter} from "@/globaltechia/utils.ts";
import ActivationsReport from "@/views/ActivationsReport.vue";
import LocalLoginView from "@/views/LocalLoginView.vue";
import LocalDashboarView from "@/views/LocalDashboardView.vue";
import UserView from "@/globaltechia/views/UserView.vue";

const local_routes = [
  {
    path: '/:app/User',
    name: 'create_user',
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
