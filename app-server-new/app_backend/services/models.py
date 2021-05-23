from django.db import models

# Create your models here.

# ------------------------------------------------------------
# ------------------------CLIENT------------------------------ 
# ------------------------------------------------------------

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    firstName = models.CharField(max_length=40)
    mail = models.CharField(max_length=80)
    registrationDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# ------------------------------------------------------------
# ------------------------BILL-------------------------------- 
# ------------------------------------------------------------

class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    issuingDate = models.DateTimeField(auto_now_add=True)
    isPaid = models.BooleanField(null=False)
    payementDate = models.DateTimeField(auto_now_add=False)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    products = models.ManyToManyField('Product', through='BillProduct')
    idClient = models.ForeignKey('Client',  on_delete=models.CASCADE)


# ------------------------------------------------------------
# ------------------------PRODUCT----------------------------- 
# ------------------------------------------------------------

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    stock = models.IntegerField()
    picture = models.CharField(max_length=80)
    price = models.DecimalField(max_digits=7, decimal_places=2)
   
    def __str__(self):
        return self.name 

class BillProduct(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.DecimalField(max_digits=7, decimal_places=2)
    idBills = models.ForeignKey('Bill', on_delete=models.CASCADE)
    idProduct = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __len__(self):
        return str(self.id)
        


        
