from django.shortcuts import render
from .forms import StandardForm
from django.contrib import messages


# Create your views here.

def standard_contact(request):
    if request.method =="POST":
        form =  StandardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("index")
    else:
        form = StandardForm()
    return render(request, 'contact/standard_contact.html', {'form':form})