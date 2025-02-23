<template>
  <div class="login-container">
    <h1>Вход</h1>
    <form @submit.prevent="handleLogin">
      <div class="form-group">
        <label for="username">Логин</label>
        <input type="text" id="username" v-model="username" required />
      </div>
      <div class="form-group">
        <label for="password">Пароль</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <button type="submit" class="login-button">Войти</button>
    </form>
    <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";

const username = ref("");
const password = ref("");
const errorMessage = ref("");
const router = useRouter();

async function handleLogin() {
  try {
    const response = await axios.post("http://localhost:8000/api/token/", {
      username: username.value,
      password: password.value,
    });

    console.log("Токен получен:", response.data.access); // Проверяем, получаем ли токен

    localStorage.setItem("token", response.data.access);
    axios.defaults.headers.common["Authorization"] = `Bearer ${response.data.access}`;

    router.push("/"); // Перенаправление на главную страницу
  } catch (error) {
    console.error("Ошибка авторизации:", error);
    errorMessage.value = "Неверный логин или пароль.";
  }
}
</script>

<style scoped>
.login-container {
  max-width: 400px;
  margin: 50px auto;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
  background: #fff;
  text-align: center;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  font-weight: bold;
}

input {
  width: 100%;
  padding: 8px;
  margin-top: 5px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.login-button {
  width: 100%;
  padding: 10px;
  background: #3498db;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.login-button:hover {
  background: #2980b9;
}

.error-message {
  color: red;
  margin-top: 10px;
}
</style>
