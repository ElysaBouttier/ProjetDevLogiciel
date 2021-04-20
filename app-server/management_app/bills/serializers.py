from bills.models import Bills, BillsProduct
from rest_framework import serializers



class BillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bills
        fields = ['id', 'idClient', 'issuingDate', 'isPaid',
                 'payementDate', 'price', 'listeProductName']


class BillsProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillsProduct
        fields = ['id', 'idBills', 'idProducts', 'quantity']
