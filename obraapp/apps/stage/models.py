from django.db import models
from project.models import Project

class Stage(models.Model):
    name = models.CharField("Name", max_length=100)
    description = models.TextField("Description", blank=True)
    order = models.IntegerField("Order")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="stages")

    class Meta:
        verbose_name = "Stage"
        verbose_name_plural = "Stages"
        ordering = ["order"]

    def __str__(self):
        return f"{self.name} - {self.project.name}"
