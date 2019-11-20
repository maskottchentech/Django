from django.db import models

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

class PollQuestions(models.Model):
	movie_list = models.CharField(choices= FILM_CHOICE,max_length=100)
	age = models.CharField(choices= AGE_CHOICE,max_length=100)
	gender = models.CharField(choices= GENDER_CHOICE,max_length=100)

	def __str__(self):
		return self.movie_list