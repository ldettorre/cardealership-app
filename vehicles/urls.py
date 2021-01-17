from django.urls import path
from . import views

urlpatterns=[
    path('', views.vehicles, name='vehicles'),

    # The url path below is commented out so that the new models can be rendered on the t_vehicle.html page. This can be undone after the search feature is working
    # path('<int:vehicle_id>', views.vehicle, name='vehicle'),
    #Test url patterns below.
    path('t_vehicles', views.t_vehicles, name='t_vehicles'),
    path('<int:carmodel_id>', views.t_vehicle, name='t_vehicle'),
]
