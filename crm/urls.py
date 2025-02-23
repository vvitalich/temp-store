from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RouteViewSet, TripStatisticViewSet, DriverWorkLogViewSet, TripViewSet

router = DefaultRouter()
router.register(r'routes', RouteViewSet)
router.register(r"trips", TripViewSet, basename="trip")
router.register(r'trip-statistics', TripStatisticViewSet)
router.register(r'driver-work-logs', DriverWorkLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
