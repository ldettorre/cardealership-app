from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('ajax_handler_carmake/<str:name>',views.ajax_handler_carmake,name='ajax_handler_carmake'),
    path('ajax_handler_carmodel/<str:carmodel>',views.ajax_handler_carmodel,name='ajax_handler_carmodel'),
]
