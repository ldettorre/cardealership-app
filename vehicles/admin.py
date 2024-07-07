from django.contrib import admin
from .models import CarMake, CarModel, CarImages
# Register your models here.


class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('id','name',)

class CarModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'make', 'model', 'color', 'engine_size', 'condition', 'year', 'price', 'published','is_featured', 'main_image')
    list_display_links = ('id', 'title')
    list_filter = ('make','condition','is_featured')
    list_editable = ('published', 'is_featured')
    list_per_page = 20
    #This allows admin to use a search feature when looking for specific vehicles
    search_fields = ('id', 'title', 'make', 'model', 'color', 'engine_size', 'condition', 'year', 'price', 'published','is_featured')

class CarImagesAdmin(admin.ModelAdmin):
    list_display = ('id','car_model',)
    search_fields = ('id',)

admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(CarImages, CarImagesAdmin)
