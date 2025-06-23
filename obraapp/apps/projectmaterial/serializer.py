from rest_framework import serializers
from .models import ProjectMaterial

class ProjectMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMaterial
        fields = '__all__'
