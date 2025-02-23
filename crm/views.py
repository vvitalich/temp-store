from rest_framework import viewsets, permissions
from .models import Route, TripStatistic, DriverWorkLog, Trip
from .serializers import RouteSerializer, TripStatisticSerializer, DriverWorkLogSerializer, TripSerializer


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(dispatcher=self.request.user)


class TripStatisticViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TripStatistic.objects.all()
    serializer_class = TripStatisticSerializer
    permission_classes = [permissions.IsAuthenticated]


class DriverWorkLogViewSet(viewsets.ModelViewSet):
    queryset = DriverWorkLog.objects.all()
    serializer_class = DriverWorkLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(manager=self.request.user)


class TripViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Trip.objects.all().order_by("departure_time")
    serializer_class = TripSerializer
    permission_classes = [permissions.AllowAny]