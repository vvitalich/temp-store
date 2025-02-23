from django.db import models
from django.contrib.auth import get_user_model
from profiles.models import Enterprise, Car

User = get_user_model()

class Route(models.Model):
    name = models.CharField(max_length=255)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE, related_name='routes')
    start_location = models.CharField(max_length=255)
    end_location = models.CharField(max_length=255)
    waypoints = models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Trip(models.Model):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]

    route = models.ForeignKey(Route, on_delete=models.CASCADE, related_name='trips')
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True, blank=True, related_name='trips')
    driver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='trips')
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')

    def __str__(self):
        return f"{self.route.name} - {self.departure_time}"

class DriverWorkLog(models.Model):
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='work_logs')
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='work_logs')
    hours_driven = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    date = models.DateField()

    def __str__(self):
        return f"{self.driver.username} - {self.date}"

class TripStatistic(models.Model):
    trip = models.OneToOneField(Trip, on_delete=models.CASCADE, related_name='statistics')
    total_passengers = models.PositiveIntegerField(default=0)
    total_revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    issues_reported = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Stats for {self.trip.route.name} ({self.trip.departure_time})"
