from django import forms  
from .models import Complainer  


class ComplainerForm(forms.ModelForm):  
    class Meta:  
        model = Complainer  
        fields = "__all__"
