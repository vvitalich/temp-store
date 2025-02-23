<template>
    <div class="trips-page">
      <div class="trips-list">
        <h2>Список рейсов</h2>
        <ul>
          <li v-for="trip in trips" :key="trip.id" class="trip-item">
            <span class="dates">{{ trip.departure_time }} - {{ trip.arrival_time }}</span>
            <span class="route">{{ trip.route_name }}</span>
            <span class="driver">{{ trip.leadDriver }}</span>
            <span class="status" :class="trip.statusClass">{{ trip.status }}</span>
          </li>
        </ul>
      </div>
      <div class="actions">
        <button class="add-trip-button" @click="addTrip">Добавить рейс</button>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted, watch } from 'vue';
  import api from "@/api";
  
  const trips = ref([]);
  const enterpriseId = ref(null);
  const routeIds = ref([]);
  
  async function fetchEnterpriseId() {
      try {
          console.log("Fetching enterprise memberships...");
          const response = await api.get("/profiles/enterprise-memberships/");
          
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
  
  async function fetchRoutes() {
      try {
          const response = await api.get("/crm/routes/");
  
          if (!enterpriseId.value || isNaN(enterpriseId.value)) {
              console.error("Enterprise ID не установлен или некорректен!");
              return;
          }
  
          routeIds.value = response.data
            .filter(route => Number(route.enterprise) === enterpriseId.value)
            .map(route => route.id);
  
          console.log("Отфильтрованные ID маршрутов:", routeIds.value);
      } catch (error) {
          console.error("Ошибка загрузки маршрутов:", error);
      }
  }
  
  async function fetchTrips() {
      try {
          const response = await api.get("/crm/trips/");
  
          trips.value = response.data
            .filter(trip => routeIds.value.includes(Number(trip.route_id)))
            .map(trip => ({
                ...trip,
                statusClass: getStatusClass(trip.status)
            }));
  
          console.log("Отфильтрованные рейсы:", trips.value);
      } catch (error) {
          console.error("Ошибка загрузки рейсов:", error);
      }
  }
  
  function getStatusClass(status) {
      switch (status) {
          case 'scheduled':
              return 'planned';
          case 'in-progress':
              return 'in-progress';
          case 'completed':
              return 'completed';
          default:
              return '';
      }
  }
  
  onMounted(fetchEnterpriseId);
  
  // Загружаем маршруты и рейсы, когда enterpriseId будет установлен
  watch(enterpriseId, async (newVal) => {
      if (newVal !== null) {
          await fetchRoutes();
          fetchTrips();
      }
  });
  </script>
  
  <style scoped>
  .trips-page {
    display: flex;
    justify-content: space-between;
    max-width: 900px;
    margin: auto;
    padding: 20px;
  }
  .trips-list {
    flex: 3;
  }
  .trips-list h2 {
    text-align: left;
    margin-bottom: 10px;
  }
  .trips-list ul {
    list-style: none;
    padding: 0;
  }
  .trip-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #f8f9fa;
    padding: 10px;
    border-radius: 5px;
    margin-bottom: 8px;
  }
  .dates {
    flex: 2;
    text-align: left;
  }
  .route {
    flex: 3;
    text-align: left;
  }
  .driver {
    flex: 2;
    text-align: left;
  }
  .status {
    flex: 1;
    text-align: center;
    font-weight: bold;
  }
  .planned {
    color: blue;
  }
  .in-progress {
    color: orange;
  }
  .completed {
    color: green;
  }
  .actions {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  .add-trip-button {
    background: #28a745;
    color: white;
    border: none;
    padding: 10px;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
  }
  .add-trip-button:hover {
    background: #218838;
  }
  </style>
  