from .models import Client

from .serializers import ClientSerializer

from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from django.shortcuts import render


# Create your views here.


# ------------------------------------------------------------------------
# ----------------------------CLIENT--------------------------------------
# ------------------------------------------------------------------------
class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ClientDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]