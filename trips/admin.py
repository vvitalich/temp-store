from django.contrib import admin
from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'passenger', 'crm_trip_id', 'seat_count', 'status', 'booking_date', 'baggage_option')
    list_filter = ('status', 'booking_date')
    search_fields = ('passenger__username', 'crm_trip_id__id')
    ordering = ('-booking_date',)

