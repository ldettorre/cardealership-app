from django.shortcuts import render, get_object_or_404
from vehicles.models import Vehicles, CarMake, CarModel
import json
from django.http import JsonResponse
from .forms import SearchForm


def index(request):
    carmakes = CarMake.objects.all()
    carmodels = CarModel.objects.all()
    form =  SearchForm(request.POST, request.FILES)
    context = {
        'carmakes' : carmakes,
        'carmodels' : carmodels,
        'form' : form,
    }
    return render(request,'home/index.html',context)

    

def about(request):
    return render(request, "home/about.html")

def blog(request):
    return render(request, "home/blog.html")

def ajax_handler(request,id):
    carmodels = CarModel.objects.filter(make_id=id).values_list('id','name')
    carmodels = dict(carmodels)
    return JsonResponse({
        'carmodels' : carmodels,
    })

def search(request):
    if 'model' in request.POST:
        id = request.POST["model"]
        
        carmodels = CarModel.objects.all()
        carmodels = carmodels.filter(id=id)
    return render(request, "home/search.html", {'carmodels':carmodels})

    
    

