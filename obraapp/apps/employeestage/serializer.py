from rest_framework import serializers
from .models import EmployeeStage

class EmployeeStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeStage
        fields = '__all__'
