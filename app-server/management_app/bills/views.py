from .models import Bills, BillsProduct

from .serializers import BillsSerializer, BillsProductSerializer

from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from django.shortcuts import render


# Create your views here.


# ------------------------------------------------------------------------
# ----------------------------BILL----------------------------------------
# ------------------------------------------------------------------------
class BillList(generics.ListCreateAPIView):
    queryset = Bills.objects.all()
    serializer_class = BillsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BillDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bills.objects.all()
    serializer_class = BillsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]