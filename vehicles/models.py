from django.db import models
from datetime import datetime

# Create your models here.


class Vehicles(models.Model):
    CONDITION_CHOICES = [("Brand New","Brand New"),("Used", "Used")]
    FUEL_CHOICES = [("Petrol","Petrol"),("Diesel", "Diesel"),("Electric", "Electric"),("Hybrid", "Hybrid")]
    TRANSMISSION_CHOICES = [("Automatic","Automatic"),("Manual", "Manual")]
    title = models.CharField(max_length=200, default = "Ad Title & Folder Name")
    def upload_photo_to(self, filename):
        return f'{self.title}/{filename}'
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.IntegerField()
    condition = models.CharField(max_length=100,blank=True, choices = CONDITION_CHOICES)
    color = models.CharField(max_length=50)
    mileage = models.IntegerField()
    fuel = models.CharField(max_length=100, choices = FUEL_CHOICES)
    engine_size = models.DecimalField(max_digits=2,decimal_places=1)
    body_type = models.CharField(max_length=100)
    owners = models.IntegerField(blank=True)
    transmission = models.CharField(max_length=100, choices = TRANSMISSION_CHOICES)
    nct_due_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
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
        return self.title



#CREATING A DEPENDENT SEARCH FORM as seen on carzone.ie

# Below are new models created to work towards a dynamic and dependent search form feature.
# The idea is to create a new 'model' for every make and model. Then based on what is available in our database, those options will be eventually be rendered via the search form fields.
# These models could then be used to revise the current vehicle form. 
# From there, the users initial selection will dictate what is to be shown in the following field. For example, if we have a Fiat in our db, then Fiat will be shown under Make and so under the following field, Model, only Fiat models will be returned. This could then expand to other fields such as Year where only those we have in the db or 'in our inventory' are provided.
# Finally, the users selection will then be passed through a view to render vehicles that match their choices on a new page where we could then look at filtering by price or other field.


#1 Create new models for searchable fields. - DONE
#2 Create a new vehicle model using the new fields. - DONE (Using CarModel)
#3 Create a new url, view and template to render the new model - DONE
#3 Create a new add via the dashboard with the new model to test that everything is working so far. - DONE
#4 Create a search form on the index page using the make and model fields. - DONE
#5 Populate the new search form using the fields above. - DONE
#6 Using JS or AJAX, work on a way to render only what is available in the db. - DONE
#7 Work on passing this submitted forms selections to a new view that renders the options on a new template.

class CarMake(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete= models.CASCADE)
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=4)

    def __str__(self):
        return '%s %s %s' % (self.make, self.name, self.year)