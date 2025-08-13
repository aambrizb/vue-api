import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// Add Theme.
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import '@fortawesome/fontawesome-free/css/all.min.css';

const app = createApp(App)

window['END_POINT'] = "http://127.0.0.1:8000/api";

app.use(router)

app.mount('#app')
