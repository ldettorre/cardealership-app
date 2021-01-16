from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator    
from .models import Vehicles, CarModel



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

def test_vehicles(request):
    vehicles = CarModel.objects.all()
    return render(request, 'vehicles/test_vehicles.html', {"vehicles":vehicles})

def test_vehicle(request, test_vehicle_id):
    vehicle = get_object_or_404(CarModel, id=test_vehicle_id)
    return render(request, 'vehicles/test_vehicle.html', {"vehicle": vehicle})