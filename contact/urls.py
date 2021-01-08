from django.urls import path
from . import views

urlpatterns=[
    path('', views.standard_contact, name='standard_contact'),
]
