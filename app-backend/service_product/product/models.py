from django.db import models

# Create your models here.

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    stock = models.IntegerField()
    picture = models.CharField(max_length=80)
    price = models.DecimalField(max_digits=7, decimal_places=2)
 