<template>
  <div class="routes-page">
    <!-- Левая колонка - список рейсов -->
    <div class="trips-list">
      <h2>Список рейсов</h2>
      <ul>
        <li v-for="trip in trips" :key="trip.id" class="trip-item">
          <span class="dates">{{ trip.startDate }} - {{ trip.endDate }}</span>
          <span class="route">{{ trip.routeName }}</span>
          <span class="driver">{{ trip.leadDriver }}</span>
          <span class="status" :class="trip.statusClass">{{ trip.status }}</span>
        </li>
      </ul>
    </div>

    <!-- Правая колонка - кнопки управления -->
    <div class="actions">
      <button class="routes-button" @click="goToRoutes">Маршруты</button>
      <button class="add-trip-button">Добавить рейс</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

const trips = ref([
  { id: 1, startDate: "10.02.2025", endDate: "12.02.2025", routeName: "Киев - Львов", leadDriver: "Иванов И.И.", status: "Запланирован", statusClass: "planned" },
  { id: 2, startDate: "11.02.2025", endDate: "13.02.2025", routeName: "Одесса - Харьков", leadDriver: "Петров П.П.", status: "В пути", statusClass: "in-progress" },
  { id: 3, startDate: "09.02.2025", endDate: "10.02.2025", routeName: "Днепр - Киев", leadDriver: "Сидоров С.С.", status: "Завершен", statusClass: "completed" },
]);

const goToRoutes = () => {
  router.push('routes');
};
</script>

<style scoped>
.routes-page {
  display: flex;
  justify-content: space-between;
  max-width: 900px;
  margin: auto;
  padding: 20px;
}

/* Левая колонка */
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

/* Правая колонка */
.actions {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.routes-button,
.add-trip-button {
  background: #007bff;
  color: white;
  border: none;
  padding: 10px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
}

.add-trip-button {
  background: #28a745;
}

.routes-button:hover {
  background: #0056b3;
}

.add-trip-button:hover {
  background: #218838;
}
</style>
