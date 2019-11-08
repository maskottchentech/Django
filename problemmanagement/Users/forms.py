from django import forms
from .models import information

class problemform(forms.ModelForm):
    class Meta:
        model = information
        fields = '__all__'  