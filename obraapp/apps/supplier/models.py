from django.db import models

class Supplier(models.Model):
    name = models.CharField("Name", max_length=100)
    cnpj = models.CharField("CNPJ", max_length=20)
    phone = models.CharField("Phone", max_length=20)
    email = models.EmailField("Email")

    class Meta:
        verbose_name = "Supplier"
        verbose_name_plural = "Suppliers"
        ordering = ["id"]

    def __str__(self):
        return self.name
