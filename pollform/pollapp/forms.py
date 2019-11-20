from django import forms
from .models import PollQuestions

FILM_CHOICE = (
	('SPIDERMAN','Spiderman'),
	('IRONMAN','Ironman'),
	('BLACK PANTHER','Black Panther'),
	('SPIDERMAN2','Spiderman2'),
	('CAPTAIN AMERICA','Captain America'),
	)

AGE_CHOICE = (
	('UNDER 18','Under 18'),
	('45-54','45-54'),
	('35-44','35-44'),
	('25-34','25-34'),
	('18-24','18-24'),
	('55-64','55-64'),
	('ABOVE 64','Above 64'),

	)

GENDER_CHOICE = (
	('MALE','Male'),
	('FEMALE','Female'),
	('OTHER','Other'),
	)

class PollForm(forms.ModelForm):
	age = forms.ChoiceField(choices=AGE_CHOICE, widget=forms.RadioSelect)
	gender = forms.ChoiceField(choices=GENDER_CHOICE, widget=forms.RadioSelect)

	class Meta:
		model = PollQuestions
		fields = '__all__'