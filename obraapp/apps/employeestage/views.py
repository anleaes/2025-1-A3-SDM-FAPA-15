from django.shortcuts import render
from rest_framework import viewsets
from .models import EmployeeStage
from .serializer import EmployeeStageSerializer

class EmployeeStageViewSet(viewsets.ModelViewSet):
    queryset = EmployeeStage.objects.all()
    serializer_class = EmployeeStageSerializer
