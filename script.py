#!/usr/bin/python3
# import requests
import os
from unicodedata import name
import django
import sys
import random



# Эти две линии очень важны, используются для поиска корня проекта, OS.Path.dirname Пропишите, сколько очков определяются в соответствии с положением файла Python, работающей отдельно
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# print(BASE_DIR)
# sys.path.append(BASE_DIR)

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'company_base.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sites.settings')
django.setup()

# from base_control.models import Person, Subject, Activity_Kind, Exchange_Answer
# from django.contrib.auth.models import User
from profiles.models import UserProfile, Enterprise, EnterpriseMembership, Car, PhoneNumber
from django.contrib.auth.models import User
# Role.objects.create(role="Passenger")


name = ['Ivan', 'Taras', 'Alex', 'Nikolay', 'Vladimir', 'Sergey', 'Dmitry', 'Evgeniy', 'Alexey', 'Petr']

for i in name:
    user = User.objects.create_user(username=i.lower(), password='revolucia@11', email=i.lower()+'@mail.ru')

    UserProfile.objects.create(user=user, first_name=i, second_name=i+'ovich')


