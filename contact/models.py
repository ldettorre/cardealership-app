from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    message = models.TextField(max_length=250)
    phone_regex = RegexValidator(regex=r'^\d+$')
    phone_number = models.CharField(validators=[phone_regex], max_length=17)
    submission_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    def __str__(self):
        return self.name


class CarSourcing(models.Model):
    CONDITION_CHOICES = [("Brand New","Brand New"),("Used", "Used")]
    FUEL_CHOICES = [("Petrol","Petrol"),("Diesel", "Diesel"),("Electric", "Electric"),("Hybrid", "Hybrid")]
    TRANSMISSION_CHOICES = [("Automatic","Automatic"),("Manual", "Manual")]
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\d+$')
    phone_number = models.CharField(validators=[phone_regex], max_length=17)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100, choices = TRANSMISSION_CHOICES)
    variant = models.CharField(max_length=100)
    year = models.IntegerField()
    condition = models.CharField(max_length=100,blank=True, choices = CONDITION_CHOICES)
    fuel = models.CharField(max_length=100, choices = FUEL_CHOICES)
    additional_information = models.TextField(max_length=250)
    gdpr_aggrement = models.BooleanField(default=True)
    submission_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    def __str__(self):
        return self.name


class EmailSubscribers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    subscription_start_date  = models.DateTimeField(blank=True, null=True, default=timezone.now)

    def __str__(self):
        return self.name
