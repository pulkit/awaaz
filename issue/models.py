from django.db import models


# Create your models here.

class issue(models.Model):
	year=models.CharField(max_length=200)
	month=models.CharField(max_length=200)
	embed=models.TextField()
