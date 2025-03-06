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
    # trip = TripSerializer(read_only=True)
    class Meta:
        model = Reservation
        fields = ('id',
                  'passenger_username',
                  'crm_trip_id',
                  'seat_count',
                  'baggage_option',
                  'booking_date',
                  'status',
                  # 'trip',
                  )

