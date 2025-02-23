from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Reservation(models.Model):
    STATUS_CHOICES = [
        ('reserved', 'Reserved'),
        ('cancelled', 'Cancelled'),
    ]

    # Пользователь, который забронировал место
    passenger = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')

    # Идентификатор рейса из CRM, к которому привязано бронирование
    crm_trip_id = models.CharField(
        max_length=255,
        help_text="Идентификатор рейса, полученный из приложения CRM"
    )

    # Количество забронированных мест (поддержка групповых бронирований)
    seat_count = models.PositiveIntegerField(default=1)

    # Дата и время бронирования
    booking_date = models.DateTimeField(auto_now_add=True)

    # Статус бронирования
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='reserved')

    # Дополнительная информация о багаже, если требуется
    baggage_option = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Опционально: выбор багажа (например, маленький, средний, большой)"
    )

    def __str__(self):
        return f"{self.passenger.username} - Рейс {self.crm_trip_id} - Мест: {self.seat_count}"
