from django.shortcuts import render, get_object_or_404
from vehicles.models import Vehicles


def index(request):
    vehicles = Vehicles.objects.all() # 
    return render(request, "home/index.html", {"vehicles":vehicles})

def about(request):
    return render(request, "home/about.html")

def blog(request):
    return render(request, "home/blog.html")