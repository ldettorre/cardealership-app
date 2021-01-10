from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    message = models.TextField(max_length=250)
   # Code below works but needs an error message because failed attempts just refresh the empty page with no warning.
    phone_regex = RegexValidator(regex=r'^\d+$')
    phone_number = models.CharField(validators=[phone_regex], max_length=17)
    submission_date = models.DateTimeField(blank=True, null=True, default=timezone.now)


    
        
