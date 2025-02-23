<template>
  <div class="dispatcher-dashboard">
    <nav class="menu">
      <ul>
        <li><router-link to="/dispatcher/movement">Маршруты и рейсы</router-link></li>
        <li><router-link to="/dispatcher/personnel">Персонал</router-link></li>
        <li><router-link to="/dispatcher/transport">Транспорт</router-link></li>
        <li><router-link to="/dispatcher/statistics">Статистика и финансы</router-link></li>
        <li><router-link to="/dispatcher/trips">Рейсы</router-link></li>
      </ul>
    </nav>

    <!-- Контент, который будет меняться в зависимости от маршрута -->
    <router-view></router-view>
  </div>
</template>

<script setup>
  // Здесь можно добавить логику для диспетчера (если потребуется)
</script>

<style scoped>
.dispatcher-dashboard {
  max-width: 900px;
  margin: 20px auto;
  padding: 20px;
  background: white; /* Фон теперь белый */
}

.menu {
  margin-bottom: 30px;
  background: #eef2f3;
  border-radius: 5px;
}

.menu ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  justify-content: space-around;
}

.menu li {
  padding: 10px 20px;
  text-align: center;
  border-radius: 5px;
}

.menu li:hover {
  background-color: #3498db;
}

.menu a {
  text-decoration: none;
  color: #333;
  font-weight: bold;
}

.menu a:hover {
  color: white;
}
</style>
