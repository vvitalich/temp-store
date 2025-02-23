from django.db import models
from django.contrib.auth.models import User

POSITIONS = [
    ("driver", "Driver"),
    ("manager", "Manager"),
    ("owner", "Owner"),
]

MESSENGER = [
    ("telegram", "Telegram"),
    ("whatsapp", "WhatsApp"),
    ("viber", "Viber"),
    ("phone", "Phone"),
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    passenger = models.BooleanField(default=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.user.username

class Enterprise(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name

class EnterpriseMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE, related_name="memberships")
    position = models.CharField(max_length=50, choices=POSITIONS)

class Car(models.Model):
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE, related_name="cars")
    model_car = models.CharField(max_length=50)
    number_car = models.CharField(max_length=50)
    passengers_capacity = models.IntegerField()
    cargo_capacity = models.IntegerField()
    has_pets_allowed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.model_car} - {self.number_car}"

class PhoneNumber(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="phones_users", null=True, blank=True)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE, related_name="phones_enterprise", null=True, blank=True)
    number = models.CharField(max_length=20)
    messenger = models.CharField(max_length=50, choices=MESSENGER)

    def __str__(self):
        return f"{self.messenger} - {self.number}"

# from django.db import models
# from django.contrib.auth.models import User
#
#
# POSITIONS = [
#     ("driver", "Driver"),
#     ("manager", "Manager"),
#     ("owner", "Owner"),
# ]
#
# MESSENGER = [
#     ("telegram", "Telegram"),
#     ("whatsapp", "WhatsApp"),
#     ("viber", "Viber"),
#     ("phone", "Phone"),
# ]
#
#
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # first_name = models.CharField(max_length=50)
#     # second_name = models.CharField(max_length=50)
#     passenger = models.BooleanField(default=True)
#     image = models.ImageField(blank=True)
#
#     def __str__(self):
#         return self.user.username
#
#
# class Enterprise(models.Model):
#     name = models.CharField(max_length=50)
#     address = models.CharField(max_length=250)
#     image = models.ImageField(blank=True)
#
#     def __str__(self):
#         return self.name
#
#
# class EnterpriseMembership(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE, related_name="memberships")
#     position = models.CharField(max_length=50,  choices=POSITIONS)
#
#
# class Car(models.Model):
#     enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE, related_name="cars")
#     model_car = models.CharField(max_length=50)
#     number_car = models.CharField(max_length=50)
#     passengers_capacity = models.IntegerField()
#     cargo_capacity = models.IntegerField()
#     has_pets_allowed = models.BooleanField(default=False)
#
#     def __str__(self):
#         return f"{self.model_car} - {self.number_car}"
#
#
# class PhoneNumber(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="phones_users", null=True, blank=True)
#     enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE, related_name="phones_enterprise", null=True, blank=True)
#     number = models.CharField(max_length=20)
#     messenger = models.CharField(max_length=50,  choices=MESSENGER)
#
#     def __str__(self):
#         return f"{self.messenger} - {self.number}"
#
