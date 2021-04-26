from django.db import models

# from django.contrib.auth.models import Client

# Create your models here.

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    firstName = models.CharField(max_length=40)
    mail = models.CharField(max_length=80)
    registrationDate = models.DateTimeField(auto_now_add=True)
 