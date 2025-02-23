<template>
    <div class="register-form">
      <h2>Регистрация</h2>
      <form @submit.prevent="handleSubmit">
        <div class="form-group">
          <label for="username">Имя пользователя</label>
          <input type="text" id="username" v-model="username" required />
        </div>
        <div class="form-group">
          <label for="email">Email</label>
          <input type="email" id="email" v-model="email" required />
        </div>
        <div class="form-group">
          <label for="password">Пароль</label>
          <input type="password" id="password" v-model="password" required />
        </div>
        <div class="form-group">
          <label for="confirm-password">Подтвердите пароль</label>
          <input type="password" id="confirm-password" v-model="confirmPassword" required />
        </div>
        <button type="submit" class="submit-button">Зарегистрироваться</button>
      </form>
      <p class="login-link">
        Уже есть аккаунт? <router-link to="/login">Войдите</router-link>
      </p>
    </div>
  </template>
  
  <script setup>
  import { ref } from "vue";
  import axios from "axios";
  import { useRouter } from "vue-router";
  
  const router = useRouter();
  
  const username = ref("");
  const email = ref("");
  const password = ref("");
  const confirmPassword = ref("");
  
  const handleSubmit = async () => {
    if (password.value !== confirmPassword.value) {
      alert("Пароли не совпадают!");
      return;
    }
  
    try {
      await axios.post("http://localhost:8000/api/register/", {
        username: username.value,
        email: email.value,
        password: password.value,
      });
      alert("Регистрация прошла успешно. Теперь вы можете войти.");
      router.push("/login");
    } catch (error) {
      console.error("Ошибка регистрации:", error);
      alert("Ошибка регистрации. Пожалуйста, проверьте введённые данные и попробуйте снова.");
    }
  };
  </script>
  
  <style scoped>
  .register-form {
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
    background: #28a745;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .submit-button:hover {
    background: #218838;
  }
  
  .login-link {
    text-align: center;
    margin-top: 10px;
  }
  </style>
  