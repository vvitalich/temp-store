from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Reservation
from .serializers import ReservationSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    """
    API для бронирования мест.
    Пассажиры видят только свои бронирования, а администраторы — все.
    """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Если пользователь — администратор, владелец или диспетчер, можно вернуть все бронирования.
        # Здесь для примера используем user.is_staff в качестве администратора.
        if user.is_staff:
            return Reservation.objects.all()
        # Иначе, пассажир видит только свои бронирования.
        return Reservation.objects.filter(passenger=user)

    def perform_create(self, serializer):
        # Автоматически устанавливаем пассажира как текущего пользователя
        serializer.save(passenger=self.request.user)

    def update(self, request, *args, **kwargs):
        """
        Позволяет обновлять бронирование. Можно использовать для отмены бронирования,
        изменяя его статус на 'cancelled'.
        """
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
