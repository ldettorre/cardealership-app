from os import access
from django.db import models
from datetime import datetime

# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Model to be revised for better image management
class CarModel(models.Model):
    CONDITION_CHOICES = [("Brand New","Brand New"),("Used", "Used")]
    COLOUR_CHOICES = [("Black","Black"),("Blue", "Blue"),("Gold", "Gold"),("Green", "Green"),("Grey", "Grey"),("Navy", "Navy"),("Orange", "Orange"),("Red", "Red"),("Silver", "Silver"),("White", "White")]
    FUEL_CHOICES = [("Petrol","Petrol"),("Diesel", "Diesel"),("Electric", "Electric"),("Hybrid", "Hybrid")]
    TRANSMISSION_CHOICES = [("Automatic","Automatic"),("Manual", "Manual"), ("Semi-auto", "Semi-auto"), ("CVT","CVT"),("Other","Other")]
    BODY_CHOICES = [("Convertible","Convertible"),("Coupe", "Coupe"), ("Estate", "Estate"), ("Hatchback","Hatchback"),("SUV","SUV"),("Saloon","Saloon")]
    title = models.CharField(max_length=200, default = "Ad Title & Folder Name")
    make = models.ForeignKey(CarMake, on_delete= models.CASCADE)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(decimal_places=2,max_digits=9)
    condition = models.CharField(max_length=100,blank=True, choices = CONDITION_CHOICES)
    color = models.CharField(max_length=100, choices = COLOUR_CHOICES)
    kilometers = models.IntegerField()
    fuel = models.CharField(max_length=100, choices = FUEL_CHOICES)
    engine_size = models.DecimalField(max_digits=2,decimal_places=1)
    body_type = models.CharField(max_length=100, choices = BODY_CHOICES)
    owners = models.IntegerField(blank=True)
    transmission = models.CharField(max_length=100, choices = TRANSMISSION_CHOICES)
    nct_due_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    is_featured = models.BooleanField(default=False)
    published = models.BooleanField(default=True)
    date_listed = models.DateTimeField(default=datetime.now)
    main_image = models.ForeignKey(
        'CarImages',
        on_delete=models.SET_NULL,
        blank=True,
        null=True)

    def __str__(self):
        return f'ID: {self.id}, Car: {self.make}, {self.model}, {self.year}'

    
class CarImages(models.Model):
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return str(self.car_model)