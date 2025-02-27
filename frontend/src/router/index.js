import { createRouter, createWebHistory } from "vue-router";
import HomePage from "../views/HomePage.vue";
import AdminDashboard from "../views/AdminDashboard.vue";
import PassengerDashboard from "../views/PassengerDashboard.vue";
import DispatcherDashboard from "../views/DispatcherDashboard.vue";
import BookingPage from "../views/BookingPage.vue";
import TransportPage from "../views/TransportPage.vue";
import PersonnelPage from "../views/PersonnelPage.vue";
import MovementPage from "../views/MovementPage.vue";
import StatisticsPage from "../views/StatisticsPage.vue";
import RoutesPage from "../views/RoutesPage.vue";
import TripsPage from "../views/TripsPage.vue";
import LoginForm from "../components/LoginForm.vue";
import RegisterForm from "../components/RegisterForm.vue";
import BookingForm from "../components/BookingForm.vue";

const routes = [
  { path: "/", component: HomePage },
  { path: "/passenger", component: PassengerDashboard },
  { path: "/bookingform", component: BookingForm },
  { path: "/booking", component: BookingPage },
  { path: "/login", component: LoginForm },
  { path: "/register", component: RegisterForm },
  { 
    path: "/administrator", 
    component: AdminDashboard,
    children: [
      { path: "transport", component: TransportPage },
      { path: "personnel", component: PersonnelPage },
      { path: "movement", component: MovementPage },
      { path: "trips", component: TripsPage },
      { path: "routes", component: RoutesPage },
      { path: "statistics", component: StatisticsPage },
    ],
  },
  { 
    path: "/dispatcher", 
    component: DispatcherDashboard,
    children: [
      { path: "transport", component: TransportPage },
      { path: "personnel", component: PersonnelPage },
      { path: "movement", component: MovementPage },
      { path: "trips", component: TripsPage },
      { path: "routes", component: RoutesPage },
      { path: "statistics", component: StatisticsPage },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
