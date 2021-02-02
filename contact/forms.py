from django import forms
from .models import Contact, CarSourcing, EmailSubscribers

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields =('name','phone_number','email','message')

class CarSourcingForm(forms.ModelForm):
    class Meta:
        model = CarSourcing
        fields =  fields = '__all__'
        exclude = ['submission_date']

class EmailSubscribersForm(forms.ModelForm):
    class Meta:
        model = EmailSubscribers
        fields =  fields = '__all__'
        exclude = ['subscription_start_date']