from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import CarModel, CarMake


def carmodels(request):
    carmodels = CarModel.objects.order_by("-price").filter(published=True)
    carmakes = CarMake.objects.all()
    paginator = Paginator(carmodels, 3)
    page = request.GET.get('page')
    paged_vehicles = paginator.get_page(page)
    context = {
        "carmodels": paged_vehicles,
        "carmakes": carmakes,
    }
    return render(request, 'vehicles/vehicles.html', context)


def carmodel(request, carmodel_id):
    carmodel = get_object_or_404(CarModel, id=carmodel_id)
    return render(request, 'vehicles/vehicle.html', {"carmodel": carmodel})


def search(request):
    carmodels = CarModel.objects.all()
    carmakes = CarMake.objects.all()

    # Filter cars by make
    if 'carmake' in request.POST:
        make = request.POST["carmake"]
        if make:
            carmodels = carmodels.filter(make__name=make)
    # Filter cars by model
    if 'carmodel' in request.POST:
        model = request.POST["carmodel"]
        if model:
            carmodels = carmodels.filter(model=model)

    # Filter cars by year
    if 'caryear' in request.POST:
        year = request.POST["caryear"]
        if year:
            carmodels = carmodels.filter(year=year)

    # Filter cars by price
    if 'price_min' in request.POST:
        price_min = request.POST["price_min"]
        if price_min == "":
            price_min = 0
    if 'price_max' in request.POST:
        price_max = request.POST["price_max"]
        if price_max == "":
            price_max = 999999
        carmodels = carmodels.filter(price__range=(price_min, price_max))

    # Filter cars by fuel type
    if 'fuel' in request.POST:
        fuel = request.POST["fuel"]
        if fuel:
            carmodels = carmodels.filter(fuel=fuel)

    # Filter cars by transmission
    if 'transmission' in request.POST:
        transmission = request.POST["transmission"]
        if transmission:
            carmodels = carmodels.filter(transmission=transmission)

    # Filter cars by engine size
    if 'engine_size_min' in request.POST:
        engine_size_min = request.POST["engine_size_min"]
        if engine_size_min == "":
            engine_size_min = 0.0
    if 'engine_size_max' in request.POST:
        engine_size_max = request.POST["engine_size_max"]
        if engine_size_max == "":
            engine_size_max = 10.0
        carmodels = carmodels.filter(
            engine_size__range=(engine_size_min, engine_size_max))

    paginator = Paginator(carmodels, 3)
    page = request.GET.get('page')
    paged_vehicles = paginator.get_page(page)
    context = {
        "carmodels": paged_vehicles,
        "carmakes": carmakes,
    }
    return render(request, 'vehicles/vehicles.html', context)

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
