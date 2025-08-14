import {getRouter} from "@/globaltechia/utils.js";
import ActivationsReport from "@/views/ActivationsReport.vue";

const local_routes = [
  {
    path: '/:app/reporte_activaciones',
    name: 'reporte_activaciones',
    component: ActivationsReport,
  }
];

const router = getRouter(local_routes);

export default router
