import Vue from "vue";
import axios from "axios"

import App from "./App.vue";
import router from "./router";

import "./assets/main.css";

axios.defaults.baseURL = "http://127.0.0.1:8000/api"

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
