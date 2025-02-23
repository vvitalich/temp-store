from rest_framework import serializers
from .models import Route, Trip, DriverWorkLog

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'


class TripStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'


class DriverWorkLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverWorkLog
        fields = '__all__'


class TripSerializer(serializers.ModelSerializer):
    route_id = serializers.CharField(source="route.id", read_only=True)
    route_name = serializers.CharField(source="route.name", read_only=True)

    class Meta:
        model = Trip
        fields = ["id", "route_id", "route_name", "departure_time", "arrival_time", "status"]