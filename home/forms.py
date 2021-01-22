from django.forms import ModelForm, modelformset_factory, formset_factory
from django import forms
from vehicles.models import CarMake, CarModel

class SearchForm(ModelForm):
    make = forms.ModelChoiceField(queryset=CarMake.objects.all(), widget=forms.Select(attrs={'class':'carmake','id':'carmake','value':'no_carmake', 'name':'carmake'}))
    model = forms.ChoiceField(widget=forms.Select(attrs={'class':'carmodel','id':'carmodel','name':'carmodel'}))
    class Meta:
        model = CarMake
        fields = ('make','model')
        