from django.contrib import admin
from .models import Vehicles, CarMake, CarModel
# Register your models here.

class VehiclesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'make', 'model', 'color', 'engine_size', 'condition', 'year', 'price', 'published')
    list_display_links = ('id', 'title')
    list_filter = ('make','condition')
    list_editable = ('published',)
    list_per_page = 20
    #This allows admin to use a search feature when looking for specific vehicles
    search_fields = ('id', 'title', 'make', 'model', 'color', 'engine_size', 'condition', 'year', 'price', 'published')


class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('id','name',)

class CarModelAdmin(admin.ModelAdmin):
    list_display = ('id','make', 'name', 'year')

admin.site.register(Vehicles, VehiclesAdmin)
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
