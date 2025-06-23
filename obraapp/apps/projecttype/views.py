from django.shortcuts import render
from rest_framework import viewsets
from .models import ProjectType
from .serializer import ProjectTypeSerializer

class ProjectTypeViewSet(viewsets.ModelViewSet):
    queryset = ProjectType.objects.all()
    serializer_class = ProjectTypeSerializer