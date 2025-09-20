import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// Add Theme.
import 'bootstrap/dist/js/bootstrap.bundle.min.js'
import 'bootstrap/dist/css/bootstrap.min.css';
import '@fortawesome/fontawesome-free/css/all.min.css';
import 'globaltechia/dist/style.css';

const app = createApp(App)

window.PROJECT_NAME    = 'SISTEMA';
window.PROJECT_TITLE   = 'SISTEMA EMPRESARIAL';
window.END_POINT       = "http://127.0.0.1:8000/api";

document.title = window.PROJECT_TITLE;

app.use(router)

app.mount('#app')
