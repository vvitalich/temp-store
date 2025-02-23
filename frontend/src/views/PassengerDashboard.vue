// PassengerDashboard.vue - Кабинет пассажира
<template>
  <div class="passenger-dashboard">
    <h1>Ваши бронирования</h1>
    <ul>
      <li v-for="booking in bookings" :key="booking.id">
        <span>{{ booking.route }} - {{ booking.date }}</span>
        <button v-if="booking.cancelable" @click="cancelBooking(booking.id)">Отменить</button>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const bookings = ref([]);

onMounted(async () => {
  // Получение списка бронирований с сервера (заглушка)
  bookings.value = [
    { id: 1, route: 'Киев → Львов', date: '2025-02-20', cancelable: true },
    { id: 2, route: 'Одесса → Харьков', date: '2025-02-25', cancelable: false }
  ];
});

const cancelBooking = (id) => {
  bookings.value = bookings.value.filter(booking => booking.id !== id);
};
</script>

<style scoped>
.passenger-dashboard {
  max-width: 600px;
  margin: 0 auto;
  text-align: center;
}
</style>