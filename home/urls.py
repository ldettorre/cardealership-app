from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('ajax_handler/<str:name>',views.ajax_handler,name='ajax_handler'),
    path('search',views.search,name='search'),
]
