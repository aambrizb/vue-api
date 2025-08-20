import {getRouter} from "@/globaltechia/utils.js";
import ActivationsReport from "@/views/ActivationsReport.vue";
import LocalLoginView from "@/views/LocalLoginView.vue";
import LocalDashboarView from "@/views/LocalDashboarView.vue";

const local_routes = [
  {
    path: '/:app/reporte_activaciones',
    name: 'reporte_activaciones',
    component: ActivationsReport,
  }
];

const router = getRouter(local_routes,LocalLoginView,LocalDashboarView);

export default router
