from .models import CarModel, CarMake


def searchFilter(request):
    carmodels = CarModel.objects.order_by("model").filter(published=True)
    carmakes = CarMake.objects.all()
    if request.method == 'GET':
        try:
            make = request.GET.get("carmake")
            model = request.GET.get("carmodel")
            year = request.GET.get("caryear")
            price_min = request.GET.get("price_min")
            if price_min == "":
                price_min = 0

            price_max = request.GET.get("price_max")
            if price_max == "":
                price_max = 999999

            fuel = request.GET.get("fuel")
            transmission = request.GET.get("transmission")

            # the filter for cars below doesn't look great but it works and
            # and uses the correct request method.
            carmodels = CarModel.objects.filter(make__name__contains=make).filter(
                model__contains=model).filter(year__contains=year).filter(
                price__range=(price_min, price_max)).filter(
                fuel__contains=fuel).filter(transmission__contains=transmission)
        except:
            carmodels = CarModel.objects.order_by(
                "model").filter(published=True)

    return carmodels
