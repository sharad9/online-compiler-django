from django.db import models

# Create your models here.
class Payload(models.Model):
	
	userName = models.CharField(max_length=50);
	language = models.CharField(max_length=50);
	code = models.TextField();
	inputs = models.TextField();
	output = models.TextField();