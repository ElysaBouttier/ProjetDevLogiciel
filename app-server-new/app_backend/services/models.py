from django.db import models

# Create your models here.

# ------------------------------------------------------------
# ------------------------BILL-------------------------------- 
# ------------------------------------------------------------

class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    issuingDate = models.DateTimeField(auto_now_add=True)
    isPaid = models.BooleanField(null=False)
    payementDate = models.DateTimeField(auto_now_add=False)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    # idClient = models.ForeignKey(Client, on_delete=models.CASCADE)


    def __str__(self):
        return self.issuingDate
 
class BillProduct(models.Model):
    id = models.AutoField(primary_key=True)
    idBills = models.ForeignKey(Bill, on_delete=models.CASCADE, blank=False, null=False)
    quantity = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.idBills



# ------------------------------------------------------------
# ------------------------CLIENT------------------------------ 
# ------------------------------------------------------------

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    firstName = models.CharField(max_length=40)
    mail = models.CharField(max_length=80)
    registrationDate = models.DateTimeField(auto_now_add=True)



# ------------------------------------------------------------
# ------------------------PRODUCT----------------------------- 
# ------------------------------------------------------------

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    stock = models.IntegerField()
    picture = models.CharField(max_length=80)
    price = models.DecimalField(max_digits=7, decimal_places=2)
 
