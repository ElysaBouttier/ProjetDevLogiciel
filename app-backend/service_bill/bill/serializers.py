from bill.models import Bill, BillProduct
from rest_framework import serializers



class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ['id', 'issuingDate', 'isPaid',
                 'payementDate', 'price']
        extra_kwargs= {'issuingDate' : {'required':False},'isPaid' : {'required':False},'payementDate' : {'required':False},'price' : {'required':True}}


class BillProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillProduct
        fields = ['id', 'idBills', 'quantity']

