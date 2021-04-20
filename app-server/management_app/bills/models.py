from django.db import models


from django.contrib.auth.models import Bills

# Create your models here.

class Bills(models.Model):
    idClient = models.ForeignKey(Client, on_delete=models.CASCADE)
    issuingDate = models.DateTimeField(auto_now_add=True)
    isPaid = models.BooleanField(null=False)
    payementDate = models.DateTimeField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    listeProductName = models.ForeignKey(BillsProduct, on_delete=models.CASCADE)


class BillsProduct(models.Model):
    idBills = models.ForeignKey(Bills, on_delete=models.CASCADE)
    idProducts = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models..IntegerField(min_value=0, max_value=300)
