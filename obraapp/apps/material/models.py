from django.db import models
from supplier.models import Supplier

class Material(models.Model):
    name = models.CharField("Name", max_length=100)
    unit = models.CharField("Unit", max_length=50)
    quantity = models.PositiveIntegerField("Quantity")
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name="materials")

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materials"
        ordering = ["id"]

    def __str__(self):
        return self.name