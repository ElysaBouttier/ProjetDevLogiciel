from django.db import models

# Create your models here.

class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    issuingDate = models.DateTimeField(auto_now_add=True)
    isPaid = models.BooleanField(null=False)
    payementDate = models.DateTimeField(auto_now_add=False)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.issuingDate
 
class BillProduct(models.Model):
    id = models.AutoField(primary_key=True)
    idBills = models.ForeignKey(Bill, on_delete=models.CASCADE, blank=False, null=False)
    quantity = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.idBills