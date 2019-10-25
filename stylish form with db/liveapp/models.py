from django.db import models

CHOICES = [
('Ambala','Ambala'),
('Chandigarh','Chandigarh'),
('Zirakpur','Zirakpur'),
]

class sampledata(models.Model):

	first_name = models.CharField(max_length=20)
	last_name  = models.CharField(max_length=20)
	city = models.CharField(choices=CHOICES,max_length=25,blank = True)
	age = models.IntegerField()
	email_id = models.EmailField(max_length=70)
	contact_num = models.IntegerField()


	def __str__(self):
		return self.first_name
