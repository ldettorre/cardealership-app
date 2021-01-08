from django import forms


class StandardForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=50)
    Message = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))