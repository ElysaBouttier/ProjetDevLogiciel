from .models import Bill, BillProduct, Client, Product

from .serializers import BillSerializer, BillProductSerializer, ClientSerializer, ProductSerializer

from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from django.shortcuts import render


# Create your views here.


# ------------------------------------------------------------------------
# ----------------------------BILL----------------------------------------
# ------------------------------------------------------------------------
class BillList(generics.ListCreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BillDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# ------------------------------------------------------------------------
# ----------------------------CLIENT--------------------------------------
# ------------------------------------------------------------------------
class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ClientDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    
# ------------------------------------------------------------------------
# ----------------------------PRODUCT-------------------------------------
# ------------------------------------------------------------------------
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]