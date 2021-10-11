from django.db import models

# Create your models here.
class Login(models.Model):
	name=models.CharField(max_length=30)
	contact=models.CharField(max_length=10)
	
	def __str__(self):
		return self.name

class Rgister(models.Model):
	name=models.CharField(max_length=30)
	contact=models.CharField(max_length=10)
	email=models.CharField(max_length=30)

	def __str__(self):
		return self.name