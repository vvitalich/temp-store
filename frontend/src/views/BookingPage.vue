<script setup>
import { ref, computed, watchEffect } from 'vue';
import { useRoute } from 'vue-router';
import { useAuthStore } from '@/stores/auth';
import api from '@/api';
import { format } from 'date-fns';
import Swal from 'sweetalert2'; // Импортируем SweetAlert2

const route = useRoute();
const authStore = useAuthStore();
// Получаем объект рейса из query-параметров
const trip = ref({});
const tripId = ref(null);
watchEffect(() => {
  try {
    trip.value = route.query.trip ? JSON.parse(route.query.trip) : {};
    tripId.value = trip.value.id ? Number(trip.value.id) : (route.query.trip_id ? Number(route.query.trip_id) : null);
  } catch (e) {
    console.error('Ошибка парсинга trip:', e);
    trip.value = {};
    tripId.value = null;
  }
  console.log('Query params:', route.query);
  console.log('Trip:', trip.value);
  console.log('Trip ID:', tripId.value);
});
const tripRoute = computed(() => trip.value.route_name || 'Неизвестный маршрут');
const tripEnterprise = computed(() => trip.value.enterprise || 'Неизвестный перевозчик');
const departureTime = computed(() => trip.value.departure_time || '');
const arrivalTime = computed(() => trip.value.arrival_time || '');
const tripStatus = computed(() => trip.value.status || '');
// Данные текущего пользователя
const name = computed(() => authStore.user?.user?.username || '');
const email = computed(() => authStore.user?.user?.email || '');
// Данные формы
const seats = ref(1);
const baggageOption = ref('');
const withPet = ref(false);
const submitBooking = async () => {
  if (!authStore.user?.user?.id) {
    Swal.fire({
      title: 'Ошибка',
      text: 'Пожалуйста, авторизуйтесь перед бронированием.',
      icon: 'error',
      confirmButtonText: 'Ок'
    });
    return;
  }
  if (!tripId.value) {
    Swal.fire({
      title: 'Ошибка',
      text: 'Ошибка: неизвестный рейс. Попробуйте снова.',
      icon: 'error',
      confirmButtonText: 'Ок'
    });
    return;
  }
  const bookingData = {
    passenger: authStore.user?.user?.id,
    crm_trip_id: tripId.value, // Передаем ID, а не объект
    seat_count: seats.value,
    booking_date: new Date().toISOString(),
    status: 'reserved',
    baggage_option: baggageOption.value,
    with_pet: withPet.value,
  };
  console.log('Отправляем бронирование:', bookingData);
  try {
    await api.post('/trips/reservations/', bookingData);
    Swal.fire({
      title: 'Успех',
      text: 'Бронирование подтверждено!',
      icon: 'success',
      confirmButtonText: 'Ок'
    }).then(() => {
      window.location.href = '/passenger'; // Переход на страницу /passenger
    });
  } catch (error) {
    console.error('Ошибка бронирования:', error);
    Swal.fire({
      title: 'Ошибка',
      text: 'Ошибка бронирования. Попробуйте снова.',
      icon: 'error',
      confirmButtonText: 'Ок'
    });
  }
};
const formatDate = (dateString) => {
  return dateString ? format(new Date(dateString), 'dd.MM.yyyy HH:mm') : 'Неизвестная дата';
};
</script>
<template>
  <div class="booking">
    <h1>Бронирование маршрута</h1>
    <p><strong>Маршрут:</strong> {{ tripRoute }}</p>
    <p><strong>Перевозчик:</strong> {{ tripEnterprise }}</p>
    <p><strong>Статус:</strong> {{ tripStatus }}</p>
    <p><strong>Дата отправления:</strong> {{ formatDate(departureTime) }}</p>
    <p><strong>Дата прибытия:</strong> {{ formatDate(arrivalTime) }}</p>
    
    <form @submit.prevent="submitBooking">
      <label>ФИО: <input :value="name" disabled /></label>
      <label>Email: <input :value="email" type="email" disabled /></label>
      <label>Количество мест: <input v-model="seats" type="number" min="1" required /></label>
      <label>Описание багажа: <input v-model="baggageOption" /></label>
      <label><input type="checkbox" v-model="withPet" /> Путешествую с животным</label>
      <button type="submit">Подтвердить бронирование</button>
    </form>
  </div>
</template>
<style scoped>
.booking {
  max-width: 500px;
  margin: 20px auto;
  padding: 15px;
  border: 1px solid #ccc;
  border-radius: 10px;
  background: #f8f9fa;
}

form {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

input, button {
  padding: 8px;
  font-size: 16px;
}

button {
  background: #3498db;
  color: white;
  border: none;
  cursor: pointer;
  border-radius: 5px;
}

button:hover {
  background: #2980b9;
}
</style>
