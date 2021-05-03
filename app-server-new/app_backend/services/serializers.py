from services.models import Bill, BillProduct, Client, Product
from rest_framework import serializers

# ------------------------------------------------------------
# ------------------------CLIENT------------------------------ 
# ------------------------------------------------------------


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'firstName', 'mail',
                 'registrationDate']


# ------------------------------------------------------------
# ------------------------BILL-------------------------------- 
# ------------------------------------------------------------

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ['id', 'issuingDate', 'isPaid',
                 'payementDate', 'price', 'listProductName', 'idClient']

class BillProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillProduct
        fields = ['id', 'quantity', 'idBills', 'idProduct']



# ------------------------------------------------------------
# ------------------------PRODUCT----------------------------- 
# ------------------------------------------------------------


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'stock',
                 'picture', 'price', 'idBills']

