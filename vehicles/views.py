from django.shortcuts import render, get_object_or_404
from .models import Vehicles

# Create your views here.

def vehicles(request):
    vehicles = Vehicles.objects.all()
    return render(request, 'vehicles/vehicles.html', {"vehicles":vehicles})

def vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicles, id=vehicle_id)
    return render(request, 'vehicles/vehicle.html', {"vehicle": vehicle})