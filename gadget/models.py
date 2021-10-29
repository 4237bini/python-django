from django.contrib.auth.models import User
from django.db import models
from django.db.models import Avg, Count
from django.forms import ModelForm
from django.urls import reverse


# Create your models here.


class Smartphone(models.Model):
   
    name = models.CharField(max_length=150, null=True, unique=True)
    display = models.CharField(max_length=255, null=True)
    processor = models.CharField(max_length=255, null=True)
    memory = models.CharField(max_length=255, null=True)
    camera = models.CharField(max_length=150, null=True)
    battery = models.CharField(max_length=150, null=True)
    colors = models.CharField(max_length=150, null=True) 
    price = models.CharField(max_length=150, null=True)
    image = models.ImageField(upload_to='img/smartphone/',null=True)
    image1 = models.ImageField(upload_to='img/smartphone/',null=True)
    image1s = models.ImageField(upload_to='img/smartphone/',null=True)
    averageRatings = models.IntegerField(default=1)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class SmartphoneDetail(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
   
    smartphone = models.ForeignKey(Smartphone, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status=models.CharField(max_length=10,choices=STATUS, default='New')
    review = models.CharField(max_length=250,blank=True)
    ratings = models.IntegerField(default=1)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

   


class Smartwatch(models.Model):
    
    name = models.CharField(max_length=150, null=True, unique=True)
    design = models.CharField(max_length=255, null=True)
    display = models.CharField(max_length=255, null=True)
    activityTracker = models.CharField(max_length=255, null=True)
    sensor = models.CharField(max_length=255, null=True)
    memory = models.CharField(max_length=150, null=True)
    battery = models.CharField(max_length=150, null=True)
    price = models.CharField(max_length=150, null=True)
    image = models.ImageField(upload_to='img/smartwatch/',null=True)
    image1 = models.ImageField(upload_to='img/smartwatch/',null=True)
    image1s = models.ImageField(upload_to='img/smartwatch/',null=True)
    averageRatings = models.IntegerField(default=1)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class SmartwatchDetail(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
   
    smartwatch = models.ForeignKey(Smartwatch, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status=models.CharField(max_length=10,choices=STATUS, default='New')
    review = models.CharField(max_length=250,blank=True)
    ratings = models.IntegerField(default=1)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True) 

class Laptop(models.Model):
   
    name = models.CharField(max_length=150, null=True, unique=True)
    display = models.CharField(max_length=255, null=True)
    processor = models.CharField(max_length=255, null=True)
    os = models.CharField(max_length=255, null=True)
    memory = models.CharField(max_length=150, null=True)
    graphics = models.CharField(max_length=150, null=True)
    storage = models.CharField(max_length=255, null=True)
    batteryLife = models.CharField(max_length=150, null=True)
    price = models.CharField(max_length=150, null=True)
    image = models.ImageField(upload_to='img/laptop/',null=True)
    image1 = models.ImageField(upload_to='img/laptop/',null=True)
    image1s = models.ImageField(upload_to='img/laptop/',null=True)
    averageRatings = models.IntegerField(default=1)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class LaptopDetail(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
   
    laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status=models.CharField(max_length=10,choices=STATUS, default='New')
    review = models.CharField(max_length=250,blank=True)
    ratings = models.IntegerField(default=1)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)            

   
