from django.shortcuts import render, redirect
from .forms import ContactForm, CarSourcingForm, EmailSubscribersForm
from django.contrib import messages
from cardealership.settings.base import EMAIL_HOST_USER
from django.core.mail import send_mail


# Create your views here.


def contact_form(request):
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("contact_form")
        else:
            messages.error(
                request, "Please ensure your phone number only contains digits")
    else:
        form = ContactForm()
    return render(request, 'contact/contact_form.html', {'form': form})


def car_sourcing(request):
    if request.method == "POST":
        form = CarSourcingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("car_sourcing")
        else:
            messages.error(
                request, "Please ensure your phone number only contains digits")
    else:
        form = CarSourcingForm()
    return render(request, 'contact/car_sourcing.html', {'form': form})


def subscribe(request):
    if request.method == "POST":
        form = EmailSubscribersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            subject = 'Welcome to Cardealership'
            message = 'Hope you are enjoying our inventory. You are receiving this email to confirm that you have now been added to our email subscription list.'
            recipient = request.POST['email']
            send_mail(subject, message, EMAIL_HOST_USER,
                      [recipient], fail_silently=False)
            context = {
                'form': form,
            }
            return redirect("index")
        
    return redirect("index")
