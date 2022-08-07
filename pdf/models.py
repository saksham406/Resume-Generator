from django.db import models

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name= models.CharField( max_length=50)
    email= models.EmailField(max_length=50)
    phone= models.CharField(max_length=15)
    summary = models.TextField(max_length=2000)
    degree= models.CharField(max_length=50)
    school= models.CharField(max_length=200)
    university=models.CharField(max_length=500)
    previous_work= models.TextField(max_length=2000)
    skills = models.CharField(max_length=1000)
    achievements= models.TextField(max_length=1000)
