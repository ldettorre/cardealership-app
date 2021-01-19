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
    return render(request,'home/index.html',context=context)

    

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