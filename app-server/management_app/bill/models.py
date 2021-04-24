from django.db import models


# from django.contrib.auth.models import Bill

# Create your models here.

class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    # idClient = models.ForeignKey(Client, on_delete=models.CASCADE)
    issuingDate = models.DateTimeField(auto_now_add=True)
    isPaid = models.BooleanField(null=False)
    payementDate = models.DateTimeField(auto_now_add=False)
    price = models.DecimalField(max_digits=7, decimal_places=2)
 