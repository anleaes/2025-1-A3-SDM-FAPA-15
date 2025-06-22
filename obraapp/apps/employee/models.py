from django.db import models

class Employee(models.Model):
    name = models.CharField("Name", max_length=100)
    position = models.CharField("Position", max_length=100)
    phone = models.CharField("Phone", max_length=20)
    email = models.EmailField("Email")

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
        ordering = ["id"]

    def __str__(self):
        return self.name