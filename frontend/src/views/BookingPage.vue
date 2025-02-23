<script setup>
import { ref, computed } from "vue";
import { useRoute } from "vue-router";

const route = useRoute();

// Получаем данные из query-параметров
const tripRoute = computed(() => route.query.route || "Неизвестный маршрут");
const tripDate = computed(() => route.query.date || "Неизвестная дата");
const tripStops = computed(() => route.query.stops ? route.query.stops.split(",") : []);

// Данные формы
const name = ref("");
const phone = ref("");
const email = ref("");
const seats = ref(1);
const withLuggage = ref(false);
const withPet = ref(false);

const submitBooking = () => {
  console.log("Бронирование подтверждено:", {
    route: tripRoute.value,
    date: tripDate.value,
    stops: tripStops.value,
    name: name.value,
    phone: phone.value,
    email: email.value,
    seats: seats.value,
    withLuggage: withLuggage.value,
    withPet: withPet.value,
  });
  alert("Бронирование подтверждено!");
};
</script>

<template>
  <div class="booking">
    <h1>Бронирование маршрута</h1>
    <p><strong>Маршрут:</strong> {{ tripRoute }}</p>
    <p><strong>Дата:</strong> {{ tripDate }}</p>
    <p><strong>Остановки:</strong> {{ tripStops.join(" → ") }}</p>

    <form @submit.prevent="submitBooking">
      <label>ФИО: <input v-model="name" required /></label>
      <label>Телефон: <input v-model="phone" required /></label>
      <label>Email: <input v-model="email" type="email" required /></label>
      <label>Количество мест: <input v-model="seats" type="number" min="1" required /></label>
      <label><input type="checkbox" v-model="withLuggage" /> С багажом</label>
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
