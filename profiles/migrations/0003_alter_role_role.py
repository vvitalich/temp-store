# Generated by Django 5.1.4 on 2025-01-09 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_phonenumber_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='role',
            field=models.CharField(choices=[('passenger', 'Passenger'), ('carrier', 'Carrier')], max_length=50),
        ),
    ]
