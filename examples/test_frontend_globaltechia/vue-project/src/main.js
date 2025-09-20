"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var vue_1 = require("vue");
var App_vue_1 = require("./App.vue");
var router_1 = require("./router");
// Add Theme.
require("bootstrap/dist/js/bootstrap.bundle.min.js");
require("bootstrap/dist/css/bootstrap.min.css");
require("@fortawesome/fontawesome-free/css/all.min.css");
require("globaltechia/dist/style.css");
var app = (0, vue_1.createApp)(App_vue_1.default);
window.PROJECT_NAME = 'SISTEMA';
window.PROJECT_TITLE = 'SISTEMA EMPRESARIAL';
window.END_POINT = "http://127.0.0.1:8000/api";
document.title = window.PROJECT_TITLE;
app.use(router_1.default);
app.mount('#app');
