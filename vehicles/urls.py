from django.urls import path
from . import views

urlpatterns=[
    path('', views.vehicles, name='vehicles'),
    path('<int:vehicle_id>', views.vehicle, name='vehicle'),
    #Test url patterns below.
    path('test_vehicles', views.test_vehicles, name='test_vehicles'),
    path('<int:test_vehicle_id>', views.test_vehicle, name='test_vehicle'),
]
