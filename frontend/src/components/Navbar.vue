<template>
  <nav class="navbar">
    <div class="logo">🚍 My Trips</div>
    <ul class="nav-links">
      <li><router-link to="/">Главная</router-link></li>
      <li v-if="userProfile && userProfile.passenger"><router-link to="/passenger">Кабинет пассажира</router-link></li>
      <li v-if="userProfile && !userProfile.passenger && !userProfile.user.is_superuser"><router-link to="/dispatcher">Кабинет диспетчера</router-link></li>
      <li v-if="userProfile && userProfile.user.is_superuser"><router-link to="/administrator">Кабинет администратора</router-link></li>
    </ul>

    <div class="auth-buttons">
      <div v-if="userProfile">
        <span class="user-info">Привет, {{ userProfile.user.username }}</span>
        <button @click="logout" class="auth-button">Выход</button>
      </div>
      <div v-else>
        <button class="auth-button" @click="goToLogin">Войти</button>
        <button class="register-button" @click="goToRegister">Регистрация</button>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref, watchEffect, onBeforeMount } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "@/stores/auth";

const router = useRouter();
const authStore = useAuthStore();
const userProfile = ref(null);

watchEffect(() => {
  userProfile.value = authStore.user;
  console.log("Обновление Navbar:", userProfile.value);
});

const handleNavigation = async () => {
  await authStore.fetchUser();
  if (userProfile.value) {
    if (userProfile.value.passenger) {
      router.push("/passenger");
    } else if (userProfile.value.user.is_superuser) {
      router.push("/administrator");
    } else {
      router.push("/dispatcher");
    }
  }
};

onBeforeMount(() => {
  handleNavigation();
});

const logout = async () => {
  await authStore.logout();
  userProfile.value = null;
  router.push("/");
};

const goToLogin = () => {
  router.push("/login");
};

const goToRegister = () => {
  router.push("/register");
};
</script>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px;
  background: #3498db;
  color: white;
}

.nav-links {
  list-style: none;
  display: flex;
  gap: 15px;
}

.nav-links li {
  display: inline;
}

.nav-links a {
  color: white;
  text-decoration: none;
}

.auth-buttons {
  display: flex;
  gap: 10px;
  align-items: center;
}

.auth-button,
.register-button {
  background: white;
  color: #3498db;
  border: none;
  padding: 8px 12px;
  cursor: pointer;
  border-radius: 5px;
  font-size: 16px;
}

.auth-button:hover,
.register-button:hover {
  background: #f1f1f1;
}

.register-button {
  background: white;
  color: #28a745;
}

.register-button:hover {
  background: #d4edda;
}

.user-info {
  margin-right: 10px;
  font-weight: bold;
}
</style>
