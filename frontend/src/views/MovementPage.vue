<template>
  <div class="routes-page">
    <!-- Левая колонка - список маршрутов -->
    <div class="routes-list">
      <h2>Список маршрутов</h2>
      <ul>
        <li v-for="route in routes" :key="route.id" class="route-item">
          <span class="route-name">{{ route.name }}</span>
          <span class="enterprise">{{ route.enterprise_name }}</span>
        </li>
      </ul>
    </div>

    <!-- Правая колонка - кнопки управления -->
    <div class="actions">
      <button class="add-route-button" @click="addRoute">Добавить маршрут</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import api from "@/api";
import { useAuthStore } from "@/stores/auth";

const routes = ref([]);
const enterpriseId = ref(null);
const authStore = useAuthStore();
const isAdmin = ref(false);

// Функция для получения роли пользователя
function checkIfAdmin() {
  isAdmin.value = authStore.user?.user?.is_superuser || false;
}

// Функция для получения ID предприятия пользователя
async function fetchEnterpriseId() {
  try {
    console.log("Fetching enterprise memberships...");
    const response = await api.get("/profiles/enterprise-memberships/");
    
    if (response.data.length === 0) {
      console.error("User has no enterprise memberships!");
      return;
    }

    const enterprise = response.data[0].enterprise;
    if (!enterprise || !enterprise.id) {
      console.error("ID предприятия не найден в объекте!");
      return;
    }

    enterpriseId.value = Number(enterprise.id);
    console.log("Enterprise ID после преобразования:", enterpriseId.value);
  } catch (error) {
    console.error("Ошибка при получении ID предприятия:", error);
  }
}

// Функция для получения маршрутов
async function fetchRoutes() {
  try {
    const response = await api.get("/crm/routes/");

    if (isAdmin.value) {
      // Администратор видит все маршруты
      routes.value = response.data;
    } else {
      // Перевозчик видит маршруты своего предприятия
      if (!enterpriseId.value || isNaN(enterpriseId.value)) {
        console.error("Enterprise ID не установлен или некорректен!");
        return;
      }

      routes.value = response.data
        .filter(route => Number(route.enterprise) === enterpriseId.value);
    }

    console.log("Отфильтрованные маршруты:", routes.value);
  } catch (error) {
    console.error("Ошибка загрузки маршрутов:", error);
  }
}

onMounted(async () => {
  checkIfAdmin();
  if (!isAdmin.value) {
    await fetchEnterpriseId();
  }
  await fetchRoutes();
});
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
.routes-list {
  flex: 3;
}

.routes-list h2 {
  text-align: left;
  margin-bottom: 10px;
}

.routes-list ul {
  list-style: none;
  padding: 0;
}

.route-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #f8f9fa;
  padding: 10px;
  border-radius: 5px;
  margin-bottom: 8px;
}

.route-name {
  flex: 3;
  text-align: left;
}

.enterprise {
  flex: 2;
  text-align: left;
  font-style: italic;
}

/* Правая колонка */
.actions {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.add-route-button {
  background: #28a745;
  color: white;
  border: none;
  padding: 10px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
}

.add-route-button:hover {
  background: #218838;
}
</style>
