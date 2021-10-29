from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    STATUS = (
        ('New', 'New'),
        ('True', 'True'),
        ('False', 'False'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(blank=True, max_length=150)
    lastname = models.CharField(blank=True, max_length=150)
    email = models.CharField(blank=True, max_length=150)
    phone = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=150)
    experience = models.CharField(blank=True, max_length=150)
    profession = models.CharField(blank=True, max_length=150)
    total = models.IntegerField(default=0)
    description = models.CharField(blank=True, max_length=255)
    profileimage = models.ImageField(blank=True, upload_to='img/user/')
    status=models.CharField(max_length=10,choices=STATUS, default='New')

