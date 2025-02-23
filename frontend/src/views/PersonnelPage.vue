<template>
  <div class="staff-page">
    <div class="header">
      <h2>Персонал</h2>
      <button class="add-button" @click="addStaffMember">Добавить</button>
    </div>
    <ul class="staff-list">
      <li v-for="staff in staffList" :key="staff.id" class="staff-item">
        <span class="name">{{ staff.lastName }} {{ staff.initials }}</span>
        <span class="position">{{ staff.position }}</span>
        <button class="assign-button" @click="assignToTrip(staff.id)">Назначить на рейс</button>
      </li>
    </ul>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const staffList = ref([
  { id: 1, lastName: "Иванов", initials: "И.И.", position: "Водитель" },
  { id: 2, lastName: "Петров", initials: "П.П.", position: "Водитель" },
  { id: 3, lastName: "Сидорова", initials: "С.С.", position: "Диспетчер" },
]);

const addStaffMember = () => {
  console.log("Добавление сотрудника");
};

const assignToTrip = (id) => {
  console.log("Назначение сотрудника на рейс", id);
};
</script>

<style scoped>
.staff-page {
  max-width: 600px;
  margin: auto;
  text-align: center;
  background: white;
  padding: 20px;
}

/* Заголовок и кнопка в одну линию */
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 15px;
}

/* Кнопка в правом верхнем углу */
.add-button {
  background: #28a745;
  color: white;
  border: none;
  padding: 10px;
  border-radius: 5px;
  cursor: pointer;
}

.staff-list {
  list-style: none;
  padding: 0;
}

.staff-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #f8f9fa;
  padding: 10px;
  border-radius: 5px;
  margin-bottom: 8px;
}

.name {
  flex: 2;
  text-align: left;
}

.position {
  flex: 1;
  text-align: center;
}

.assign-button {
  background: #007bff;
  color: white;
  border: none;
  padding: 5px 10px;
  border-radius: 5px;
  cursor: pointer;
}

.assign-button:hover {
  background: #0056b3;
}
</style>
