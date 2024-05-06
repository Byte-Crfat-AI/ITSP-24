from django.db import models

# Create your models here.

class User(models.Model):
    userid=models.IntegerField()
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=100)

class Device(models.Model):
    deviceid=models.ForeignKey(User, on_delete=models.CASCADE)
