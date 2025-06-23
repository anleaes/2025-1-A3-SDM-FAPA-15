from django.db import models
from project.models import Project
from material.models import Material

class ProjectMaterial(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="project_materials")
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name="project_usages")
    quantity_used = models.PositiveIntegerField("Quantity Used")

    class Meta:
        verbose_name = "Project Material"
        verbose_name_plural = "Project Materials"
        unique_together = ('project', 'material')
        ordering = ["id"]

    def __str__(self):
        return f"{self.material.name} used in {self.project.name}"
