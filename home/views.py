from django.shortcuts import render, get_object_or_404
from vehicles.models import Vehicles, CarMake, CarModel
import json
from django.http import JsonResponse
# from .forms import SearchForm


def index(request):
    carmakes = CarMake.objects.all()
    carmodels = CarModel.objects.all()
    context = {
        'carmakes' : carmakes,
        'carmodels' : carmodels,
    }
    return render(request,'home/index.html',context)

    

def about(request):
    return render(request, "home/about.html")

def blog(request):
    return render(request, "home/blog.html")

def ajax_handler(request,name):
    carMakeName = name

    carmodels = CarModel.objects.filter(make__name=carMakeName).values_list('id','name',)
    carmodels = dict(carmodels)
    listK =[]
    listV =[]
    for val in carmodels.values():
        if val in listK:
            continue
        else:
            listK.append(val)
            listV.append(val)
    carmodels = dict(zip(listK, listV))
    # print(carmodels)
    
    return JsonResponse({
        'carmodels' : carmodels,
    })

# Code Below gets the year!
    # name = carmodels[0][1]
    # carmodels = CarModel.objects.filter(name=name).values_list('id','year')


def search(request):
    carmodels = CarModel.objects.all()
    if 'carmodel' in request.POST:
        name = request.POST["carmodel"]
        print(name)
        if name:
            carmodels = carmodels.filter(name=name)
    context ={
        'carmodels':carmodels,
    }
    return render(request, "home/search.html", {'carmodels':carmodels})



    