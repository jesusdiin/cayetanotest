import Vue from "vue";
import VueRouter from "vue-router";
import HomeView from "../views/HomeView.vue";
import Recetario from "../views/Recetarios.vue";
import RecetarioId from "../views/RecetarioId.vue";
import NewRecetario from '../views/NewRecetario.vue'

Vue.use(VueRouter);

const router = new VueRouter({
  mode: "history",
  base: import.meta.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/bebidas",
      name: "bebidas",
      component: () => import("../views/BebidasList.vue")
    },
    {
      path: "/recetarios",
      name: "recetarios",
      component: Recetario,
    },
    {
      path: '/recetarios/new',
      name: 'recetarioNew',
      component: NewRecetario
    },
    {
      path: '/recetarios/:id',
      name: 'recetarioId',
      component: RecetarioId
    },
  ],
});

export default router;
