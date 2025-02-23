<template>
    <div class="transport-page">
      <div class="header">
        <button @click="showAddVehicleModal" class="add-button">Добавить +</button>
      </div>
  
      <div class="content">
        <!-- Блок характеристик автомобиля (слева) -->
        <div class="vehicle-details" v-if="selectedVehicle">
          <h2>Характеристики</h2>
          <p><strong>Модель:</strong> {{ selectedVehicle.model }}</p>
          <p><strong>Год выпуска:</strong> {{ selectedVehicle.year }}</p>
          <p><strong>Марка:</strong> {{ selectedVehicle.brand }}</p>
          <p><strong>Цвет:</strong> {{ selectedVehicle.color }}</p>
          <p><strong>Номерной знак:</strong> {{ selectedVehicle.licensePlate }}</p>
          <p><strong>Макс. пассажиров:</strong> {{ selectedVehicle.maxPassengers }}</p>
        </div>
  
        <!-- Список автомобилей (справа) -->
        <div class="vehicle-list">
          <ul>
            <li v-for="vehicle in vehicles" :key="vehicle.id" class="vehicle-item">
              <div @click="selectVehicle(vehicle)" class="vehicle-info">
                <span><strong>{{ vehicle.model }}</strong></span> —
                <span>№ {{ vehicle.licensePlate }}</span> —
                <span>{{ vehicle.year }}</span>
              </div>
              <button @click="assignToRoute(vehicle)" class="assign-button">Назначить на маршрут</button>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  // Модели данных
  const vehicles = ref([
    { id: 1, model: 'Ford Transit', year: 2018, brand: 'Ford', color: 'Белый', licensePlate: 'AA1234BB', maxPassengers: 15 },
    { id: 2, model: 'Mercedes Sprinter', year: 2020, brand: 'Mercedes', color: 'Серый', licensePlate: 'CC5678DD', maxPassengers: 12 },
    { id: 3, model: 'Renault Master', year: 2019, brand: 'Renault', color: 'Черный', licensePlate: 'EE9012FF', maxPassengers: 10 },
  ]);
  
  // Состояния
  const selectedVehicle = ref(null);
  
  // Выбор автомобиля для отображения его характеристик
  const selectVehicle = (vehicle) => {
    selectedVehicle.value = vehicle;
  };
  
  // Назначение автомобиля на маршрут (заглушка)
  const assignToRoute = (vehicle) => {
    alert(`Автомобиль ${vehicle.model} назначен на маршрут!`);
  };
  </script>
  
  <style scoped>
  .transport-page {
    padding: 20px;
  }
  
  .header {
    display: flex;
    justify-content: flex-end;
  }
  
  .add-button {
    background-color: #3498db;
    color: white;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .add-button:hover {
    background-color: #2980b9;
  }
  
  .content {
    display: flex;
    gap: 20px;
    margin-top: 20px;
  }
  
  /* Блок характеристик автомобиля (слева) */
  .vehicle-details {
    width: 30%;
    background-color: #eef2f3;
    padding: 15px;
    border-radius: 5px;
  }
  
  /* Список автомобилей (справа) */
  .vehicle-list {
    flex-grow: 1;
  }
  
  .vehicle-item {
    background-color: #f8f9fa;
    padding: 10px;
    margin-bottom: 10px;
    border-radius: 5px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  
  .vehicle-info {
    cursor: pointer;
  }
  
  .assign-button {
    background-color: #2ecc71;
    color: white;
    padding: 5px 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .assign-button:hover {
    background-color: #27ae60;
  }
  </style>
  