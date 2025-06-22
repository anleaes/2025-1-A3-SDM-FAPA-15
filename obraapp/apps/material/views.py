from django.shortcuts import render
from rest_framework import viewsets
from .models import Material
from .serializer import MaterialSerializer

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
