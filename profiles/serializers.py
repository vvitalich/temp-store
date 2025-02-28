from rest_framework import serializers
from .models import UserProfile, PhoneNumber, Enterprise, EnterpriseMembership, Car
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_superuser']


class UserProfileSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user')
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'user','user_id', 'passenger', 'image']

    def create(self, validated_data):
        user = validated_data.pop('user')
        user_profile = UserProfile.objects.create(user=user, **validated_data)
        return user_profile


class EnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enterprise
        fields = ['id', 'name', 'address', 'image']


class EnterpriseMembershipSerializer(serializers.ModelSerializer):
    enterprise = EnterpriseSerializer(read_only=True)  # Вложенный сериализатор для предприятия

    class Meta:
        model = EnterpriseMembership
        fields = ['user', 'enterprise', 'position']


class CarSerializer(serializers.ModelSerializer):
    enterprise = EnterpriseSerializer(read_only=True)  # Вложенный сериализатор для предприятия

    class Meta:
        model = Car
        fields = ['model_car', 'number_car', 'enterprise', 'passengers_capacity', 'cargo_capacity', 'has_pets_allowed']


class PhoneNumberSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # Сериализуем как строку (имя пользователя)
    enterprise = EnterpriseSerializer(read_only=True)  # Вложенный сериализатор для предприятия

    class Meta:
        model = PhoneNumber
        fields = ['user', 'enterprise', 'number', 'messenger']


