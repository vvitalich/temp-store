<template>
    <div class="auth-container">
      <h2>Регистрация</h2>
      <form @submit.prevent="register">
        <div class="form-group">
          <label for="email">Email:</label>
          <input type="email" id="email" v-model="email" required />
        </div>
  
        <div class="form-group">
          <label for="password">Пароль:</label>
          <input type="password" id="password" v-model="password" required />
        </div>
  
        <div class="form-group">
          <label for="confirmPassword">Подтвердите пароль:</label>
          <input type="password" id="confirmPassword" v-model="confirmPassword" required />
        </div>
  
        <button type="submit" class="auth-button">Зарегистрироваться</button>
  
        <p class="switch-auth">Уже есть аккаунт? <router-link to="/login">Войти</router-link></p>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  
  const email = ref('');
  const password = ref('');
  const confirmPassword = ref('');
  const router = useRouter();
  
  const register = () => {
    if (password.value !== confirmPassword.value) {
      alert("Пароли не совпадают!");
      return;
    }
  
    console.log("Регистрация:", email.value, password.value);
    // Здесь можно реализовать логику регистрации через API
    router.push('/login');
  };
  </script>
  
  <style scoped>
  .auth-container {
    max-width: 400px;
    margin: auto;
    padding: 20px;
    text-align: center;
  }
  
  .form-group {
    margin-bottom: 15px;
    text-align: left;
  }
  
  label {
    display: block;
    font-weight: bold;
  }
  
  input {
    width: 100%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  .auth-button {
    width: 100%;
    padding: 10px;
    background: #28a745;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
  }
  
  .auth-button:hover {
    background: #218838;
  }
  
  .switch-auth {
    margin-top: 10px;
  }
  </style>
  