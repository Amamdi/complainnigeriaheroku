from django import forms
from django.forms import ModelForm

from . import models
from .models import Complainer


class ComplainerForm(forms.ModelForm):  
    class Meta:
        model = Complainer
        fields = "__all__"
        # fields = ['user', 'date', 'anonymous', 'firstname', 'lastname', 'state', 'complaintIsAgainst', 'natureOfComplaint', 'complaint', 'images']

# class UploadForm(forms.ModelForm):
#     class Meta:
#         model = Complainer
#         fields = Complainer.images


class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )











