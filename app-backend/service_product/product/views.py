from .models import Product

from .serializers import ProductSerializer

from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from django.shortcuts import render


# Create your views here.


# ------------------------------------------------------------------------
# ----------------------------PRODUCT-------------------------------------
# ------------------------------------------------------------------------
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]