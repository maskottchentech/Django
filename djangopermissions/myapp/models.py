from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.utils import timezone 
from django.contrib.auth.models import User


class Article(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()

	def __str__(self):
		return self.title




 
