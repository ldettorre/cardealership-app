from django.db import models
from datetime import datetime
import os
# Create your models here.


class Vehicles(models.Model):
    CONDITION_CHOICES = [("Brand New","Brand New"),("Used", "Used")]
    FUEL_CHOICES = [("Petrol","Petrol"),("Diesel", "Diesel"),("Electric", "Electric"),("Hybrid", "Hybrid")]
    TRANSMISSION_CHOICES = [("Automatic","Automatic"),("Manual", "Manual")]
    title = models.CharField(max_length=200, default = "Place Title For Ad Here")
    def folder_name(self, title):
        return self.title
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.IntegerField()
    condition = models.CharField(max_length=100,blank=True, choices = CONDITION_CHOICES)
    color = models.CharField(max_length=100)
    mileage = models.IntegerField()
    fuel = models.CharField(max_length=100, choices = FUEL_CHOICES)
    engine_size = models.DecimalField(max_digits=2,decimal_places=1)
    body_type = models.CharField(max_length=100)
    owners = models.IntegerField(blank=True)
    transmission = models.CharField(max_length=100, choices = TRANSMISSION_CHOICES)
    nct_due_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_1 = models.ImageField(upload_to='photos/self.title', blank=True)
    photo_2 = models.ImageField(upload_to=folder_name, blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_7 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_8 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_9 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_10 = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    published = models.BooleanField(default=True)
    date_listed = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

