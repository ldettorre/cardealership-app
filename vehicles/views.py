from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator    
from .models import Vehicles

# Create your views here.

def vehicles(request):
    vehicles = Vehicles.objects.order_by("-price").filter(published=True)
    paginator = Paginator(vehicles, 3)
    page = request.GET.get('page')
    paged_vehicles = paginator.get_page(page)
    return render(request, 'vehicles/vehicles.html', {"vehicles":paged_vehicles})

def vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicles, id=vehicle_id)
    return render(request, 'vehicles/vehicle.html', {"vehicle": vehicle})