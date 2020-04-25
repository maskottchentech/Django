from django import forms
from .models import Person

class PersonData(forms.Form):
	class meta:
		model = Person
		fields = '__all__'