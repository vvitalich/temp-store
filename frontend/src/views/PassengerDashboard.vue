// PassengerDashboard.vue - Кабинет пассажира
<template>
  <div class="passenger-dashboard">
    <h1>Ваши бронирования</h1>
    <ul>
      <li v-for="booking in bookings" :key="booking.id">
        <span>{{ booking.route_name }} - {{ formatDate(booking.departure_time) }}</span>
        <button v-if="booking.cancelable" @click="cancelBooking(booking.id)">Отменить</button>
      </li>
    </ul>
    <div v-if="loading" class="loading">Загрузка...</div>
    <div v-if="error" class="error">{{ error }}</div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import api from '@/api'; // Импортируем ваш API модуль
import { format } from 'date-fns';

const bookings = ref([]);
const loading = ref(false);
const error = ref('');

const fetchBookings = async () => {
  loading.value = true;
  error.value = '';
  try {
    const response = await api.get('/trips/reservations/'); // Запрос списка бронирований
    const tripIds = response.data.map(booking => booking.crm_trip_id);
    const tripsResponse = await api.get(`/trips/?ids=${tripIds.join(',')}`); // Запрос данных о рейсах
    const tripsData = tripsResponse.data;

    // Объединяем данные бронирований с данными рейсов
    bookings.value = response.data.map(booking => {
      const trip = tripsData.find(trip => trip.id === booking.crm_trip_id);
      return {
        ...booking,
        route_name: trip.route_name,
        departure_time: trip.departure_time,
        cancelable: booking.status === 'reserved' // Делаем кнопку отмены доступной только если статус 'reserved'
      };
    });
  } catch (err) {
    error.value = 'Ошибка при загрузке бронирований.';
    console.error('Ошибка при загрузке бронирований:', err);
  } finally {
    loading.value = false;
  }
};

const cancelBooking = async (id) => {
  try {
    await api.delete(`/trips/reservations/${id}/`); // Запрос на отмену бронирования
    bookings.value = bookings.value.filter(booking => booking.id !== id);
  } catch (err) {
    error.value = 'Ошибка при отмене бронирования.';
    console.error('Ошибка при отмене бронирования:', err);
  }
};

const formatDate = (dateString) => {
  return dateString ? format(new Date(dateString), 'dd.MM.yyyy HH:mm') : 'Неизвестная дата';
};

onMounted(fetchBookings);
</script>

<style scoped>
.passenger-dashboard {
  max-width: 600px;
  margin: 0 auto;
  text-align: center;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  margin: 10px 0;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background: #f8f9fa;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

button {
  background: #e74c3c;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 5px;
  padding: 5px 10px;
}

button:hover {
  background: #c0392b;
}

.loading, .error {
  color: red;
  margin-top: 20px;
}
</style>
