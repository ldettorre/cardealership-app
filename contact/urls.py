from django.urls import path
from . import views

urlpatterns=[
    path('', views.contact_form, name='contact_form'),
    path('car_sourcing', views.car_sourcing, name='car_sourcing'),

]
