from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from vehicles.models import CarMake, CarModel
import json
from django.http import JsonResponse
from contact.forms import EmailSubscriberForm

def index(request):
    makes = CarModel.objects.all()
    current_makes = []
    for m in makes:
        current_makes.append(m.make.name)
    current_avail_makes = set(current_makes)
    carmakes = CarMake.objects.all()
    carmodels = CarModel.objects.all()
    featured_cars = CarModel.objects.filter(is_featured=True)
    if request.method =="POST":
        form =  EmailSubscriberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = EmailSubscriberForm()
    context = {
        'current_avail_makes': current_avail_makes,
        'carmakes': carmakes,
        'carmodels': carmodels,
        'form': form,
        'featured_cars': featured_cars,
    }
    return render(request, 'home/index.html', context)


def about(request):
    return render(request, "home/about.html")


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

