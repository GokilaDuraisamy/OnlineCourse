from django.db import models

# Create your models here.
class contactusform(models.Model):
    fname = models.CharField(max_length=255,blank=True, null=True,)
    empid= models.EmailField(max_length=255,blank=True, null=True,unique=True,)
    message = models.TextField(blank=True, null=True,)
   
class Enquiry(models.Model):
    name = models.CharField(max_length=255,blank=True, null=True,)
    email= models.EmailField(max_length=255,blank=True, null=True,unique=True,)
    courses = models.CharField(max_length=255,blank=True, null=True,)
    message = models.TextField(blank=True, null=True,)