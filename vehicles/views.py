from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator    
from .models import Vehicles, CarModel, CarMake



def vehicles(request):
    vehicles = Vehicles.objects.order_by("-price").filter(published=True)
    paginator = Paginator(vehicles, 3)
    page = request.GET.get('page')
    paged_vehicles = paginator.get_page(page)
    return render(request, 'vehicles/vehicles.html', {"vehicles":paged_vehicles})

def vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicles, id=vehicle_id)
    return render(request, 'vehicles/vehicle.html', {"vehicle": vehicle})


#Test views below

def t_vehicles(request):
    carmodels = CarModel.objects.all()
    return render(request, 'vehicles/t_vehicles.html', {"carmodels":carmodels})

def t_vehicle(request, carmodel_id):
    carmodel = get_object_or_404(CarModel, id=carmodel_id)
    return render(request, 'vehicles/t_vehicle.html', {"carmodel": carmodel})