from django.db import models

# Create your models here.

class Carouseldata(models.Model):

	heading = models.CharField(max_length=30)
	text_field = models.CharField(max_length=250)
	image = models.FileField(upload_to='uploads/')
