from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from cardealership.settings.prod import MEDIA_URL
from .models import CarModel, CarMake, CarImages
from .forms import CarModelForm
from .utils import searchFilter
from django.db.models import Q
import os
from django.conf import settings


def carmodels(request):
    makes = CarModel.objects.order_by("model").filter(published=True)
    current_makes = []
    for m in makes:
        current_makes.append(m.make.name)
    current_avail_makes = set(current_makes)
    carmodels = searchFilter(request)

    paginator = Paginator(carmodels, 3)
    page = request.GET.get('page')
    paged_vehicles = paginator.get_page(page)
    # Change carmodels variable to paged_vehicles in order to use pagination
    context = {
        "current_avail_makes":current_avail_makes,
        "carmodels": carmodels
    }
    return render(request, 'vehicles/vehicles.html', context)






from cardealership.settings.prod import *
DATABASE_URL = config("DATABASE_URL")
import boto3
from decouple import config

# def carmodel(request, carmodel_id):
#     carmodel = get_object_or_404(CarModel, id=carmodel_id)
#     folder_name = carmodel.title.replace(" ", '%20')
#     image_folder = MEDIA_URL+carmodel.title
#     print("THIS IS THE TITLE", carmodel.title)
    
#     images =[]
#     cli = boto3.resource('s3',aws_access_key_id=config("AWS_ACCESS_KEY_ID"),
#     aws_secret_access_key=config("AWS_SECRET_ACCESS_KEY"))
#     bucket = cli.Bucket('cardealership-app')
#     for i in bucket.objects.filter(Prefix='media/'+carmodel.title):
#         print(i.key)
#         images.append(i.key)

    
    
#     # The folders within the cardealership bucket are actually objects and not more buckets. So 
#     # i need to iterate over objects in a bucket and not over buckets.

#     return render(request, 'vehicles/vehicle.html', {"carmodel": carmodel, "image_folder":image_folder, "folder_name":folder_name,"images":images})

# Test view to render images from carImages model
def carmodel(request, carmodel_id):
    carmodel = get_object_or_404(CarModel, id=carmodel_id)
    carImages = CarImages.objects.filter(ad_title=carmodel)
    for i in carImages:
        print(i.images.url)

    folder_name = carmodel.title.replace(" ", '%20')
    image_folder = MEDIA_URL+carmodel.title
    print("THIS IS THE TITLE", carmodel.title)
    
    images =[]
    cli = boto3.resource('s3',aws_access_key_id=config("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=config("AWS_SECRET_ACCESS_KEY"))
    bucket = cli.Bucket('cardealership-app')
    for i in bucket.objects.filter(Prefix='media/'+carmodel.title):
        print(i.key)
        images.append(i.key)

    
    
    # The folders within the cardealership bucket are actually objects and not more buckets. So 
    # i need to iterate over objects in a bucket and not over buckets.
    context = {
        "carmodel": carmodel, 
        "image_folder":image_folder, 
        "folder_name":folder_name,
        "images":images,
        "carImages":carImages
    }
    return render(request, 'vehicles/vehicle.html', context)






def ajax_handler_carmake(request, name):
    carMakeName = name
    carmodels = CarModel.objects.filter(
        make__name=carMakeName).values_list('id', 'model',)
    carmodels = dict(carmodels)
    listK = []
    listV = []
    for val in carmodels.values():
        if val in listK:
            continue
        else:
            listK.append(val)
            listV.append(val)
    carmodels = dict(zip(listK, listV))
    return JsonResponse({
        'carmodels': carmodels,
    })


def ajax_handler_carmodel(request, carmodel):
    carModelName = carmodel
    caryears = CarModel.objects.filter(
        model=carModelName).values_list('id', 'year',)
    caryears = dict(caryears)
    listK = []
    listV = []
    for val in caryears.values():
        if val in listK:
            continue
        else:
            listK.append(val)
            listV.append(val)
    caryears = dict(zip(listK, listV))
    return JsonResponse({
        'caryears': caryears,
    })


def addVehicle(request):
    form = CarModelForm()
    if request.method == 'POST':
        form = CarModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
    }
    return render(request, 'vehicles/add_vehicle.html', context)
