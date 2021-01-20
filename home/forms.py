from django.forms import ModelForm, modelformset_factory, formset_factory
from django import forms
from vehicles.models import CarMake, CarModel

class SearchForm(ModelForm):
    name = forms.ModelChoiceField(queryset=CarMake.objects.all(), widget=forms.Select(attrs={'class':'carmake','id':'carmake','value':'no_carmake'}))
    make = forms.ChoiceField(widget=forms.Select(attrs={'class':'carmodel','id':'carmodel'}))
    class Meta:
        model = CarMake
        fields = ('name','make')
        