from django.db import models

# from django.contrib.auth.models import Client

# Create your models here.

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=None, min_length=None, allow_blank=False)
    mail = models.CharField(max_length=None, min_length=None, allow_blank=False)
    registrationDate = models.DateTimeField(auto_now_add=True)
 