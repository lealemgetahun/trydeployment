
from django.db import models

class Classify(models.Model):
	image = models.ImageField(upload_to="images", blank=True, null=True)
	# spam = models.IntegerField()
	def __str__(self):
		return "image"	

class responce(models.Model):
# Create your models here.
	spam = models.IntegerField()
	def __str__(self):
		return "image"	