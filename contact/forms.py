from django import forms
from .models import Contact, CarSourcing, EmailSubscriber

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields =('name','phone_number','email','message')

class CarSourcingForm(forms.ModelForm):
    class Meta:
        model = CarSourcing
        fields =  fields = '__all__'
        exclude = ['submission_date']

class EmailSubscriberForm(forms.ModelForm):
    class Meta:
        model = EmailSubscriber
        fields =  fields = '__all__'
        exclude = ['subscription_start_date']