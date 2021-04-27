from bill.models import Bill
from rest_framework import serializers



class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ['id', 'issuingDate', 'isPaid',
                 'payementDate', 'price']

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ['id', 'idBills', 'quantity']

