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

def ajax_handler(request,id):
    carmodels = CarModel.objects.filter(make_id=id).values_list('id','name')
    print(carmodels)
    carmodels = dict(carmodels)
    return JsonResponse({
        'carmodels' : carmodels,
    })

# Code Below gets the year!
    # name = carmodels[0][1]
    # carmodels = CarModel.objects.filter(name=name).values_list('id','year')


def search(request):
    if 'carmodel' in request.POST:
        id = request.POST["carmodel"]
        print(id)
        carmodels = CarModel.objects.all()
        carmodels = carmodels.filter(id=id)
    return render(request, "home/search.html", {'carmodels':carmodels})
