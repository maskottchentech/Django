from django.db import models

class APIData(models.Model):
	name = models.CharField(max_length=50)
	Home = models.CharField(max_length=50)
