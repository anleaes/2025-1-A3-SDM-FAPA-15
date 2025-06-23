from django.db import models
class ProjectType(models.Model):
    name = models.CharField("Name", max_length=100)
    description = models.TextField("Description", blank=True)

    class Meta:
        verbose_name = "Project Type"
        verbose_name_plural = "Project Types"
        ordering = ["id"]

    def __str__(self):
        return self.name
