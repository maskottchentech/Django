from django import forms
from .models import sampledata

class formdata(forms.ModelForm):
	class Meta:
		model = sampledata
		fields = '__all__'