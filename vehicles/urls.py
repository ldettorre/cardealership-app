from django.urls import path
from . import views

urlpatterns=[
    path('', views.carmodels, name='carmodels'),
    path('<int:carmodel_id>', views.carmodel, name='carmodel'),
    path('add_vehicle', views.addVehicle, name='add_vehicle'),
]
