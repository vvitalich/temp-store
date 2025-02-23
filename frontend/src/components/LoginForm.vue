<template>
    <div class="login-form">
      <h2>Войти</h2>
      <form @submit.prevent="handleSubmit">
        <div class="form-group">
          <label for="username">Имя пользователя</label>
          <input type="text" id="username" v-model="username" required />
        </div>
        <div class="form-group">
          <label for="password">Пароль</label>
          <input type="password" id="password" v-model="password" required />
        </div>
        <button type="submit" class="submit-button">Войти</button>
      </form>
      <p class="register-link">
        Нет аккаунта? <router-link to="/register">Зарегистрируйтесь</router-link>
      </p>
    </div>
  </template>
  
  <script setup>
  import { ref } from "vue";
  import { useAuthStore } from "@/stores/auth";
  import { useRouter } from "vue-router";
  
  const authStore = useAuthStore();
  const router = useRouter();
  
  const username = ref("");
  const password = ref("");
  
  const handleSubmit = async () => {
    try {
      await authStore.login(username.value, password.value);
      router.push("/"); // Переход на главную страницу после успешного входа
    } catch (error) {
      console.error("Ошибка входа:", error);
      alert("Ошибка входа. Пожалуйста, проверьте ваши данные и попробуйте снова.");
    }
  };
  </script>
  
  <style scoped>
  .login-form {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background: #fff;
  }
  
  .form-group {
    margin-bottom: 15px;
  }
  
  .form-group label {
    display: block;
    margin-bottom: 5px;
  }
  
  .form-group input {
    width: 100%;
    padding: 10px;
    box-sizing: border-box;
  }
  
  .submit-button {
    width: 100%;
    padding: 10px;
    background: #3498db;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .submit-button:hover {
    background: #2980b9;
  }
  
  .register-link {
    text-align: center;
    margin-top: 10px;
  }
  </style>
  