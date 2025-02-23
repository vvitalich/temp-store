<template>
  <div class="routes-page">
    <div class="routes-list">
      <h2>Список маршрутов</h2>
      <ul>
        <li v-for="route in routes" :key="route.id" class="route-item">
          <span class="route-name">{{ route.name }}</span>
          <span class="route-note">{{ route.start_location }} → {{ route.end_location }}</span>
        </li>
      </ul>
    </div>
    <div class="actions">
      <button class="add-route-button" @click="addRoute">Добавить маршрут</button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import { useAuthStore } from '@/stores/auth';
import api from "@/api";

const authStore = useAuthStore();
const routes = ref([]);
const enterpriseId = ref(null);

async function fetchEnterpriseId() {
    try {
        console.log("Fetching enterprise memberships...");
        const response = await api.get("/profiles/enterprise-memberships/");
        
        console.log("Enterprise memberships response:", response.data);
        console.log("Полный объект предприятия:", response.data[0]); 

        if (response.data.length === 0) {
            console.error("User has no enterprise memberships!");
            return;
        }

        const enterprise = response.data[0].enterprise;  // Достаем объект enterprise
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

async function fetchRoutes() {
    try {
        const response = await api.get("/crm/routes/");
        console.log("Все маршруты с сервера:", response.data);

        if (!enterpriseId.value || isNaN(enterpriseId.value)) {
            console.error("Enterprise ID не установлен или некорректен!");
            return;
        }

        console.log("Фильтруем маршруты по Enterprise ID:", enterpriseId.value);

        routes.value = response.data.filter(route => Number(route.enterprise) === enterpriseId.value);
        console.log("Отфильтрованные маршруты:", routes.value);
    } catch (error) {
        console.error("Ошибка загрузки маршрутов:", error);
    }
}

onMounted(fetchEnterpriseId);

// Загружаем маршруты, когда enterpriseId будет установлен
watch(enterpriseId, (newVal) => {
    if (newVal !== null) {
        fetchRoutes();
    }
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
flex: 2;
text-align: left;
font-weight: bold;
}
.route-note {
flex: 3;
text-align: left;
font-style: italic;
}
.actions {
flex: 1;
display: flex;
flex-direction: column;
gap: 10px;
}
.add-route-button {
background: #007bff;
color: white;
border: none;
padding: 10px;
border-radius: 5px;
cursor: pointer;
font-size: 16px;
}
.add-route-button:hover {
background: #0056b3;
}
</style>
