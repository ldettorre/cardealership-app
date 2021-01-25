from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator    
from .models import CarModel, CarMake

def carmodels(request):
    carmodels = CarModel.objects.order_by("-price").filter(published=True)
    paginator = Paginator(carmodels, 3)
    page = request.GET.get('page')
    paged_vehicles = paginator.get_page(page)
    return render(request, 'vehicles/vehicles.html', {"carmodels":paged_vehicles})

def carmodel(request, carmodel_id):
    carmodel = get_object_or_404(CarModel, id=carmodel_id)
    return render(request, 'vehicles/vehicle.html', {"carmodel": carmodel})
    