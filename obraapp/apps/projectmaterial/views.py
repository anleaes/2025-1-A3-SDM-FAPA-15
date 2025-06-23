from django.shortcuts import render
from rest_framework import viewsets
from .models import ProjectMaterial
from .serializer import ProjectMaterialSerializer

class ProjectMaterialViewSet(viewsets.ModelViewSet):
    queryset = ProjectMaterial.objects.all()
    serializer_class = ProjectMaterialSerializer
