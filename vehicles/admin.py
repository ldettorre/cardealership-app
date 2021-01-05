from django.contrib import admin
from .models import Vehicles
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'price', 'year')
    search_fields = ('make', 'model', 'price', 'year')#This allows admin to use a search feature when looking for specific products

admin.site.register(Vehicles)