from django.urls import path
from . import views

urlpatterns=[
    path('', views.carmodels, name='carmodels'),
    path('<int:carmodel_id>', views.carmodel, name='carmodel'),
    path('search',views.search,name='search'),
]
