from django.shortcuts import render, get_object_or_404, HttpResponse
from vehicles.models import CarMake, CarModel
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
    carmodels = CarModel.objects.filter(make__name=carMakeName).values_list('id','model',)
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
    
    return JsonResponse({
        'carmodels' : carmodels,
    })

def ajax_handler2(request,carmodel): 
    carModelName = carmodel
    caryears = CarModel.objects.filter(model=carModelName).values_list('id','year',)
    caryears = dict(caryears)
    listK =[]
    listV =[]
    for val in caryears.values():
        if val in listK:
            continue
        else:
            listK.append(val)
            listV.append(val)
    caryears = dict(zip(listK, listV))

    print(caryears)
    return JsonResponse({
        'caryears' : caryears,
    })
    

def search(request):
    carmodels = CarModel.objects.all()

    #Filter cars by make
    if 'carmake' in request.POST:
        make = request.POST["carmake"]
        if make:
            carmodels = carmodels.filter(make__name=make)

    #Filter cars by model
    if 'carmodel' in request.POST:
        model = request.POST["carmodel"]
        if model:
            carmodels = carmodels.filter(model=model)
    
    #Filter cars by year
    if 'caryear' in request.POST:
        year = request.POST["caryear"]
        if year:
            carmodels = carmodels.filter(year=year)

    context ={
        'carmodels':carmodels,
    }
    return render(request, "vehicles/vehicles.html", {'carmodels':carmodels})



    