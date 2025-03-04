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
import api from '@/api';
import { format, isValid } from 'date-fns';

const bookings = ref([]);
const loading = ref(false);
const error = ref('');

const fetchBookings = async () => {
  loading.value = true;
  error.value = '';
  try {
    const response = await api.get('/trips/reservations/');
    console.log('Reservations:', response.data);
    
    const tripIds = [...new Set(response.data.map(booking => booking.crm_trip_id))]; // Убираем дубликаты
    if (tripIds.length === 0) {
      bookings.value = response.data;
      return;
    }

    const tripsResponse = await api.get(`/crm/trips/?ids=${tripIds.join(',')}`);
    console.log('Trips:', tripsResponse.data);
    
    const tripsData = Array.isArray(tripsResponse.data) ? tripsResponse.data : [];
    
    bookings.value = response.data.map(booking => {
      const trip = tripsData.find(trip => trip.id === booking.crm_trip_id);
      return {
        ...booking,
        route_name: trip ? trip.route_name : 'Маршрут не найден',
        departure_time: trip ? trip.departure_time : null,
        cancelable: booking.status === 'reserved'
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
    await api.delete(`/trips/reservations/${id}/`);
    bookings.value = bookings.value.filter(booking => booking.id !== id);
  } catch (err) {
    error.value = 'Ошибка при отмене бронирования.';
    console.error('Ошибка при отмене бронирования:', err);
  }
};

const formatDate = (dateString) => {
  if (!dateString) return 'Дата неизвестна';
  const date = new Date(dateString);
  return isValid(date) ? format(date, 'dd.MM.yyyy HH:mm') : 'Некорректная дата';
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
