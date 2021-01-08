from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages


# Create your views here.

def contact_form(request):
    return render(request, 'contact/contact_form.html', {'form':form})