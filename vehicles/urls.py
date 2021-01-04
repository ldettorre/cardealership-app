from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='vehicles'),
    path('<int:vehicle_id', views.vehicle, name='vehicle'),
]
