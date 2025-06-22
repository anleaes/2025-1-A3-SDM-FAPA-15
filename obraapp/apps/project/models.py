from django.db import models
from projecttype.models import ProjectType

class Project(models.Model):
    name = models.CharField("Name", max_length=100)
    description = models.TextField("Description", blank=True)
    start_date = models.DateField("Start Date")
    in_progress = models.BooleanField("In Progress", default=True)
    project_type = models.ForeignKey(ProjectType, on_delete=models.CASCADE, related_name="projects")

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
        ordering = ["id"]

    def __str__(self):
        return self.name
