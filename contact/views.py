from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages


# Create your views here.

def contact_form(request):
    if request.method =="POST":
        form =  ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("contact_form")
    else:
        form = ContactForm()
    return render(request, 'contact/contact_form.html', {'form':form})