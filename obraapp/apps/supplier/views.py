from django.shortcuts import render
from rest_framework import viewsets
from .models import Supplier
from .serializer import SupplierSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
