from django.forms import ModelForm
from django import forms
from .models import CarModel

class CarModelForm(ModelForm):
    class Meta:
        model = CarModel
        fields = '__all__'