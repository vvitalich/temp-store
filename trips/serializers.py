from rest_framework import serializers
from .models import Reservation
from crm.models import Trip

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    passenger_username = serializers.CharField(source="passenger.username", read_only=True)
    crm_trip_id = serializers.PrimaryKeyRelatedField(queryset=Trip.objects.all())  # Ожидает ID

    class Meta:
        model = Reservation
        fields = '__all__'

