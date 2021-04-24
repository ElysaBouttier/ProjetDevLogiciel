from bill.models import Bill
from rest_framework import serializers



class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ['id', 'idClient', 'issuingDate', 'isPaid',
                 'payementDate', 'price', 'listeProductName']

