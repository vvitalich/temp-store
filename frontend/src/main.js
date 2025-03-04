// main.js
import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import { createPinia } from "pinia";
// Импортируйте Bootstrap и BootstrapVue 3
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.bundle';
import BootstrapVue3 from 'bootstrap-vue-3';

// Импортируйте стили BootstrapVue 3
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css';

const app = createApp(App);
const pinia = createPinia();
app.use(pinia);
app.use(router);
app.use(BootstrapVue3);
app.mount("#app");
