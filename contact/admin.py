from django.contrib import admin
from .models import Contact, CarSourcing

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'submission_date')

class CarSourcingAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'submission_date')
 
admin.site.register(Contact, ContactAdmin)
admin.site.register(CarSourcing, CarSourcingAdmin)