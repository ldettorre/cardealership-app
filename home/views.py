from django.shortcuts import render


def index(request):
    return render(request, "home/index.html")

def about(request):
    return render(request, "home/about.html")

def faq(request):
    return render(request, "home/faq.html")