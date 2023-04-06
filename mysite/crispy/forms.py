from django import forms
from django.core import validators
class BasicForm(forms.Form):
    title = forms.CharField(validators=[validators.MinLengthValidator(2, "title should be atleast 2")])
    
    mileage = forms.IntegerField()
    purchase_date = forms.DateField()