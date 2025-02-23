from django.contrib import admin
from .models import Route, Trip, DriverWorkLog, TripStatistic

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ('name', 'enterprise', 'start_location', 'end_location', 'created_at', 'updated_at')
    search_fields = ('name', 'start_location', 'end_location')
    # list_filter = ('enterprise',)

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ( 'driver', 'departure_time', 'arrival_time', 'status')  #'route',
    search_fields = ('route__name', 'driver__username',)
    list_filter = ('status', 'departure_time')

@admin.register(DriverWorkLog)
class DriverWorkLogAdmin(admin.ModelAdmin):
    list_display = ('driver', 'trip', 'hours_driven', 'date')
    search_fields = ('driver__username', 'trip__route__name',)
    list_filter = ('date',)

@admin.register(TripStatistic)
class TripStatisticsAdmin(admin.ModelAdmin):
    list_display = ('trip', 'total_passengers', 'total_revenue')
    search_fields = ('trip__route__name',)
    list_filter = ('trip__status',)
