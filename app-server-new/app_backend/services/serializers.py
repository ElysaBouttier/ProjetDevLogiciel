from services.models import Bill, BillProduct, Client, Product
from rest_framework import serializers

# ------------------------------------------------------------
# ------------------------BILL-------------------------------- 
# ------------------------------------------------------------


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ['id', 'idClient', 'issuingDate', 'isPaid',
                 'payementDate', 'price', 'listeProductName']

class BillProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillProduct
        fields = ['id', 'idBills', 'quantity']

# ------------------------------------------------------------
# ------------------------CLIENT------------------------------ 
# ------------------------------------------------------------


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'issuingDate', 'isPaid',
                 'payementDate', 'price', 'listeProductName']


# ------------------------------------------------------------
# ------------------------PRODUCT----------------------------- 
# ------------------------------------------------------------


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'stock',
                 'picture', 'price']

