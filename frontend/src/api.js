import axios from "axios";
import { useAuthStore } from "@/stores/auth";

const api = axios.create({
    baseURL: "http://127.0.0.1:8000/api/",
});

// Автоматически добавляем токен в заголовки
api.interceptors.request.use((config) => {
    const authStore = useAuthStore();
    const token = authStore.token; // Проверяем токен из Pinia
    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
});

export default api;
