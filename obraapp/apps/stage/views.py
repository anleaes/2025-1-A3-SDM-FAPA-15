from django.shortcuts import render
from rest_framework import viewsets
from .models import Stage
from .serializer import StageSerializer

class StageViewSet(viewsets.ModelViewSet):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer
