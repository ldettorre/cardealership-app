from .models import CarModel, CarMake


def searchFilter(request):
    carmodels = CarModel.objects.order_by("model").filter(published=True)
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

    return carmodels