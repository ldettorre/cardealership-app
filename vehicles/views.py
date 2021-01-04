from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'vehicles/vehicles.html')

def vehicle(request):
    return render(request, 'vehicles/vehicle.html')