from rest_framework import serializers
from .models import Route, Trip, DriverWorkLog

class RouteSerializer(serializers.ModelSerializer):
    enterprise_name = serializers.CharField(source="enterprise.name", read_only=True)
    class Meta:
        model = Route
        fields = [
            "id",
            "name",
            "start_location",
            "end_location",
            "waypoints",
            "created_at",
            "updated_at",
            "enterprise",
            "enterprise_name"
        ]


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
    enterprise = serializers.CharField(source="route.enterprise", read_only=True)


    class Meta:
        model = Trip
        fields = [
            "id",
            "route_id",
            "route_name",
            "enterprise",
            "departure_time",
            "arrival_time",
            "status"
        ]