<template>
  <div class="home">
    <h1>Ближайшие маршруты</h1>
    <ul class="trip-list">
      <li v-for="trip in trips" :key="trip.id" class="trip-item">
        <span class="route">{{ trip.route_name }}</span>
        <span class="date">{{ formatDate(trip.departure_time) }}</span>
        <button @click="handleBooking(trip)" class="book-button">
          Забронировать
        </button>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";
import { useAuthStore } from "@/stores/auth"; // Убедитесь, что вы импортировали ваш authStore

const trips = ref([]);
const router = useRouter();
const authStore = useAuthStore();

const fetchTrips = async () => {
  try {
    const response = await axios.get("http://localhost:8000/api/crm/trips/");
    trips.value = response.data;
  } catch (error) {
    console.error("Ошибка загрузки маршрутов", error);
  }
};

const formatDate = (dateString) => {
  const options = { year: "numeric", month: "long", day: "numeric" };
  return new Date(dateString).toLocaleDateString("ru-RU", options);
};

const handleBooking = (trip) => {
  if (authStore.user) {
    router.push({
      path: '/booking',
      query: {
        route: trip.route_name,
        date: trip.departure_time,
        trip_id: trip.id,
        passengers_capacity: trip.passengers_capacity
      },
    });
  } else {
    router.push('/login');
  }
};

onMounted(fetchTrips);
</script>

<style scoped>
.home {
  text-align: center;
}

.trip-list {
  list-style: none;
  padding: 0;
  max-width: 800px;
  margin: 0 auto;
}

.trip-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #f8f9fa;
  padding: 10px;
  border-radius: 8px;
  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
  margin-bottom: 10px;
}

.route {
  flex: 2;
  text-align: left;
  font-weight: bold;
}

.date {
  flex: 1;
  text-align: center;
}

.book-button {
  flex: 1;
  padding: 6px 10px;
  background: #3498db;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  text-align: center;
}

.book-button:hover {
  background: #2980b9;
}
</style>
