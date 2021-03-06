from django.shortcuts import render, redirect
from .forms import ContactForm, CarSourcingForm, EmailSubscriberForm
from django.contrib import messages
from cardealership.settings.base import EMAIL_HOST_USER
from django.core.mail import send_mail
from .models import EmailSubscriber
from decouple import config



# Create your views here.


def contact_form(request):
    confirmation_message = "Thank you for filling out our contact form! \n A member of our team will be in touch within 24 hours to assist you with your query."
    if request.method == "POST":
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            person = request.POST['name']
            phone_number = request.POST['phone_number']
            email = request.POST['email']
            submitted_message = request.POST['message']
            subject = 'You have a new contact submission'
            message = 'Hi, you received a new message from '+ person + '. '+'Please contact them via ' + phone_number + ' or ' + email + ' about the following message: ' + submitted_message 
            recipient = config('EMAIL_ADDRESS')
            send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
            return render(request, "contact/success.html", {'confirmation_message':confirmation_message})

        else:
            messages.error(
                request, "Please ensure your phone number only contains digits")
    else:
        form = ContactForm()
    return render(request, 'contact/contact_form.html', {'form': form})


def car_sourcing(request):
    confirmation_message = "Thank you for filling out our car sourcing form. We are excited to help you find exactly what you are looking for! A member of our team will contact you shortly about taking the next step!."
    if request.method == "POST":
        form = CarSourcingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "contact/success.html", {'confirmation_message':confirmation_message})
        else:
            messages.error(
                request, "Please ensure your phone number only contains digits")
    else:
        form = CarSourcingForm()
    return render(request, 'contact/car_sourcing.html', {'form': form})


def subscribe(request):
    confirmation_message = "Thank you for subscribing to our newsletter."

    if request.method == "POST":
        form = EmailSubscriberForm(request.POST, request.FILES)
        submitted_email = request.POST['email']

        # If the submitted email exists, don't save it.
        if EmailSubscriber.objects.filter(email=submitted_email).exists():
            return render(request, "contact/success.html", {'confirmation_message':confirmation_message})

        # If it doesn't exist and is valid, save it and send the email.
        elif form.is_valid():
            form.save()
            subject = 'Welcome to Cardealership'
            message = 'Hope you\'re enjoying our inventory. You are receiving this email to confirm that you have now been added to our email subscription list.'
            recipient = request.POST['email']
            send_mail(subject, message, EMAIL_HOST_USER, [recipient], fail_silently=False)
            return render(request, "contact/success.html", {'confirmation_message':confirmation_message})
        
    return render(request, "contact/success.html")
