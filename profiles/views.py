from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.exceptions import NotAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

from .models import UserProfile, Enterprise, EnterpriseMembership, Car, PhoneNumber
from .serializers import UserProfileSerializer, EnterpriseSerializer, EnterpriseMembershipSerializer, CarSerializer, PhoneNumberSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            raise NotAuthenticated("Вы не авторизованы")
        return UserProfile.objects.filter(user=self.request.user)

    def list(self, request, *args, **kwargs):
        """Возвращает профиль текущего пользователя, а не список всех"""
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response({"detail": "Профиль не найден"}, status=404)
        serializer = self.get_serializer(queryset.first())
        return Response(serializer.data)


class EnterpriseViewSet(viewsets.ModelViewSet):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer


class EnterpriseMembershipViewSet(viewsets.ModelViewSet):
    serializer_class = EnterpriseMembershipSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return EnterpriseMembership.objects.none()  # Пустой набор данных для анонимного пользователя
        # Получаем только членства текущего пользователя
        return EnterpriseMembership.objects.filter(user=self.request.user)


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class PhoneNumberViewSet(viewsets.ModelViewSet):
    serializer_class = PhoneNumberSerializer
    permission_classes = [IsAuthenticated]  # Ограничиваем доступ только авторизованным пользователям

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return PhoneNumber.objects.none()  # Возвращаем пустой набор данных для анонимного пользователя
        # Получаем только номера текущего пользователя
        return PhoneNumber.objects.filter(user=self.request.user)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_info(request):
    user = request.user
    return Response({"id": user.id, "username": user.username})

