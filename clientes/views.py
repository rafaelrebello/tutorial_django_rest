from django.shortcuts import render
from rest_framework import viewsets
from clientes.serializers import ClienteSerializer
from clientes.models import Cliente

# Create your views here.


class ClientesViewSet(viewsets.ModelViewSet):
    """"Listando Clientes"""

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
