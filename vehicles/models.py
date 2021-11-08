from django.db import models
from datetime import datetime

# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CarModel(models.Model):
    CONDITION_CHOICES = [("Brand New","Brand New"),("Used", "Used")]
    COLOUR_CHOICES = [("Black","Black"),("Blue", "Blue"),("Gold", "Gold"),("Green", "Green"),("Grey", "Grey"),("Navy", "Navy"),("Orange", "Orange"),("Red", "Red"),("Silver", "Silver"),("White", "White")]
    FUEL_CHOICES = [("Petrol","Petrol"),("Diesel", "Diesel"),("Electric", "Electric"),("Hybrid", "Hybrid")]
    TRANSMISSION_CHOICES = [("Automatic","Automatic"),("Manual", "Manual"), ("Semi-auto", "Semi-auto"), ("CVT","CVT"),("Other","Other")]
    BODY_CHOICES = [("Convertible","Convertible"),("Coupe", "Coupe"), ("Estate", "Estate"), ("Hatchback","Hatchback"),("SUV","SUV"),("Saloon","Saloon")]
    title = models.CharField(max_length=200, default = "Ad Title & Folder Name")
    def upload_photo_to(self, filename):
        print(filename)
        return f'{self.title}/{filename}'
    make = models.ForeignKey(CarMake, on_delete= models.CASCADE)
    model = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    price = models.IntegerField()
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
    photo_main = models.ImageField(upload_to=upload_photo_to, blank=True)
    photo_1 = models.ImageField(upload_to=upload_photo_to, blank=True)
    photo_2 = models.ImageField(upload_to=upload_photo_to, blank=True)
    photo_3 = models.ImageField(upload_to=upload_photo_to, blank=True)
    photo_4 = models.ImageField(upload_to=upload_photo_to, blank=True)
    photo_5 = models.ImageField(upload_to=upload_photo_to, blank=True)
    photo_6 = models.ImageField(upload_to=upload_photo_to, blank=True)
    photo_7 = models.ImageField(upload_to=upload_photo_to, blank=True)
    photo_8 = models.ImageField(upload_to=upload_photo_to, blank=True)
    photo_9 = models.ImageField(upload_to=upload_photo_to, blank=True)
    photo_10 = models.ImageField(upload_to=upload_photo_to, blank=True)
    published = models.BooleanField(default=True)
    date_listed = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return '%s %s %s' % (self.make, self.model, self.year)

    


