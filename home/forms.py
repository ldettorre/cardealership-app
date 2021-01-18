from django.forms import ModelForm, modelformset_factory, formset_factory
from django import forms
from vehicles.models import CarMake

class CarMakeForm(ModelForm):
    name = forms.CharField(widget=forms.Select)
    class Meta:
        model = CarMake
        fields = ('name',)