from django.shortcuts import render, redirect
from .forms import ContactForm, CarSourcingForm
from django.contrib import messages


# Create your views here.
def contact_form(request):
    if request.method =="POST":
        form =  ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("contact_form")
        else:
            messages.error(request, "Please ensure your phone number only contains digits")
    else:
        form = ContactForm()
    return render(request, 'contact/contact_form.html', {'form':form})

def car_sourcing(request):
    if request.method =="POST":
        form =  CarSourcingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("car_sourcing")
        else:
            messages.error(request, "Please ensure your phone number only contains digits")
    else:
        form = CarSourcingForm()
    return render(request, 'contact/car_sourcing.html', {'form':form})