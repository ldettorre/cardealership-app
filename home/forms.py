# from django.forms import ModelForm, modelformset_factory, formset_factory
# from django import forms
# from vehicles.models import CarMake, CarModel

# class SearchForm(ModelForm):
#     make = forms.ModelChoiceField(queryset=CarMake.objects.all(), widget=forms.Select(attrs={'class':'carmake','id':'carmake','value':'no_carmake', 'name':'carmake'}))
#     model = forms.ChoiceField(widget=forms.Select(attrs={'class':'carmodel','id':'carmodel','name':'carmodel', 'value':'Any Model'}))
#     year = forms.ChoiceField(widget=forms.Select(attrs={'class':'year','id':'year','name':'year'}))
#     class Meta:
#         model = CarMake
#         fields = ('make','model', 'year')
        




# This is commented out because I want to try to get the form working with dynamic fields first being created via html, then moved over to a form.