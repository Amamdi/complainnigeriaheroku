from django import forms
from django.forms import ModelForm
from .models import Complainer  


class ComplainerForm(forms.ModelForm):  
    class Meta:  
        model = Complainer  
        fields = "__all__"


class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )











