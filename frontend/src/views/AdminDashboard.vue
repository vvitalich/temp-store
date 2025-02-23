<template>
    <div class="dispatcher-dashboard">
      <nav class="menu">
        <ul>
          <li><router-link to="/dispatcher/trips">Рейсы</router-link></li>
          <li><router-link to="/dispatcher/movement">Маршруты</router-link></li>
          <li><router-link to="/dispatcher/personnel">Персонал</router-link></li>
          <li><router-link to="/dispatcher/transport">Транспорт</router-link></li>
          <li><router-link to="/dispatcher/statistics">Статистика и финансы</router-link></li>
  
        </ul>
      </nav>
  
      <!-- Контент, который будет меняться в зависимости от маршрута -->
      <router-view></router-view>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted, watch } from 'vue';
  import { useAuthStore } from '@/stores/auth';
  import api from "@/api";
  
  const authStore = useAuthStore();
  const trips = ref([]);
  const enterpriseId = ref(null);
  
  async function fetchEnterpriseId() {
      try {
          console.log("Fetching enterprise memberships...");
          const response = await api.get("/profiles/enterprise-memberships/");
          
          console.log("Enterprise memberships response:", response.data);
          if (response.data.length === 0) {
              console.error("User has no enterprise memberships!");
              return;
          }
  
          const enterprise = response.data[0].enterprise;
          if (!enterprise || !enterprise.id) {
              console.error("ID предприятия не найден в объекте!");
              return;
          }
  
          enterpriseId.value = Number(enterprise.id);
          console.log("Enterprise ID после преобразования:", enterpriseId.value);
      } catch (error) {
          console.error("Ошибка при получении ID предприятия:", error);
      }
  }
  
  async function fetchTrips() {
      try {
          const response = await api.get("/crm/trips/");
          console.log("Все рейсы с сервера:", response.data);
  
          if (!enterpriseId.value || isNaN(enterpriseId.value)) {
              console.error("Enterprise ID не установлен или некорректен!");
              return;
          }
  
          console.log("Фильтруем рейсы по Enterprise ID:", enterpriseId.value);
  
          trips.value = response.data.filter(trip => Number(trip.enterprise) === enterpriseId.value);
          console.log("Отфильтрованные рейсы:", trips.value);
      } catch (error) {
          console.error("Ошибка загрузки рейсов:", error);
      }
  }
  
  onMounted(fetchEnterpriseId);
  
  watch(enterpriseId, (newVal) => {
      if (newVal !== null) {
          fetchTrips();
      }
  });
  </script>
    
  <style scoped>
  .dispatcher-dashboard {
    max-width: 900px;
    margin: 20px auto;
    padding: 20px;
    background: white; /* Фон теперь белый */
  }
  
  .menu {
    margin-bottom: 30px;
    background: #eef2f3;
    border-radius: 5px;
  }
  
  .menu ul {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    justify-content: space-around;
  }
  
  .menu li {
    padding: 10px 20px;
    text-align: center;
    border-radius: 5px;
  }
  
  .menu li:hover {
    background-color: #3498db;
  }
  
  .menu a {
    text-decoration: none;
    color: #333;
    font-weight: bold;
  }
  
  .menu a:hover {
    color: white;
  }
  </style>
  