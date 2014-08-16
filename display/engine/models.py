from django.db import models

class forex(models.Model):
	date=models.DateField();
	rate=models.FloatField();

class idata(models.Model):
	Date=models.CharField(max_length=6);
	ADBL=models.FloatField();
	RBB=models.FloatField();
	NBL=models.FloatField();
	IR=models.FloatField();
	FOREX=models.FloatField();
	GoldPrice=models.FloatField();
	Petrol=models.FloatField();
# Create your models here.

class GD(models.Model):
	Date = models.CharField(max_length=6);
	GDP = models.FloatField();
	GNI = models.FloatField();
