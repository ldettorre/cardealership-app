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
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'})
        }

        # These are set to blank because I want the placeholder to identify each field. 
        # After testing, the form still works as intended.
        labels = {
            "name": "",
            "email": ""
        }
