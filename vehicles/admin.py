from django.contrib import admin
from .models import Vehicles
# Register your models here.

class VehiclesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'make', 'model', 'color', 'engine_size', 'condition', 'year', 'price', 'published')
    list_display_links = ('id', 'title')
    list_filter = ('make','condition')
    list_editable = ('published',)
    list_per_page = 20
    search_fields = ('id', 'title', 'make', 'model', 'color', 'engine_size', 'condition', 'year', 'price', 'published')#This allows admin to use a search feature when looking for specific vehicles

admin.site.register(Vehicles, VehiclesAdmin)