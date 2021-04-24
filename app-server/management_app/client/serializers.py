from bill.models import Client
from rest_framework import serializers



class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'issuingDate', 'isPaid',
                 'payementDate', 'price', 'listeProductName']

