from django.db import models

# Create your models here.
class Books(models.Model):
	title = models.CharField(max_length=200)
	serial_number = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	year = models.CharField(max_length=30)
def __str__(self):
	return self.title