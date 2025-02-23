// stores/auth.js
import { defineStore } from "pinia";
import axios from "axios";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    token: localStorage.getItem("token") || null,
    user: null,
  }),
  actions: {
    async login(username, password) {
      try {
        const response = await axios.post("http://localhost:8000/api/token/", {
          username,
          password,
        });
        this.token = response.data.access;
        localStorage.setItem("token", response.data.access);
        await this.fetchUser();
        this.$router.push("/");
      } catch (error) {
        console.error("Ошибка авторизации:", error);
      }
    },
    async fetchUser() {
      if (this.token) {
        try {
          const response = await axios.get("http://localhost:8000/api/profiles/user-profiles/", {
            headers: { Authorization: `Bearer ${this.token}` },
          });
          this.user = response.data;
        } catch (error) {
          console.error("Ошибка получения данных пользователя:", error);
          this.user = null;
        }
      }
    },
    logout() {
      this.token = null;
      this.user = null;
      localStorage.removeItem("token");
      window.location.reload();
    },
  },
});
