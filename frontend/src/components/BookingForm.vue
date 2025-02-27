<template>
    <div class="booking-form">
      <h2>Заказ места в рейсе</h2>
      <form @submit.prevent="submitBooking">
        <div class="form-group">
          <label for="trip">Выберите рейс:</label>
          <select v-model="selectedTrip" id="trip">
            <option v-for="trip in trips" :key="trip.id" :value="trip.id">
              {{ trip.route_name }} ({{ formatDate(trip.departure_time) }} - {{ formatDate(trip.arrival_time) }})
            </option>
          </select>
        </div>
        <div class="form-group">
          <label for="seatCount">Количество мест:</label>
          <input type="number" id="seatCount" v-model="seatCount" min="1" />
        </div>
        <div class="form-group">
          <label for="baggage">Описание багажа:</label>
          <input type="text" id="baggage" v-model="baggageOption" />
        </div>
        <button type="submit">Заказать</button>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import api from '@/api';
  import { format } from 'date-fns';
  
  const trips = ref([]);
  const selectedTrip = ref(null);
  const seatCount = ref(1);
  const baggageOption = ref('');
  const userId = ref(16);  // Предположим, что идентификатор пользователя известен и равен 16
  
  const fetchTrips = async () => {
    const response = await api.get('/api/trips/');
    trips.value = response.data;
  }
  
  const submitBooking = async () => {
    const bookingData = {
      passenger: userId.value,
      crm_trip_id: selectedTrip.value,
      seat_count: seatCount.value,
      booking_date: new Date().toISOString(),
      status: 'reserved',
      baggage_option: baggageOption.value,
    };
  
    await api.post('/api/trips/reservations/', bookingData);
    alert('Бронирование успешно создано!');
  }
  
  const formatDate = (dateString) => {
    return format(new Date(dateString), 'dd.MM.yyyy HH:mm');
  }
  
  onMounted(fetchTrips);
  </script>
  
  <style scoped>
  .booking-form {
    max-width: 400px;
    margin: auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  label {
    display: block;
    margin-bottom: 5px;
  }
  
  input, select {
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
  }
  
  button {
    width: 100%;
    padding: 10px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #218838;
  }
  </style>
  