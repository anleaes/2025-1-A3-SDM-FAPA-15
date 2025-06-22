from django.db import models
from employee.models import Employee
from stage.models import Stage

class EmployeeStage(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='stages')
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE, related_name='employees')

    class Meta:
        verbose_name = "Employee Assignment"
        verbose_name_plural = "Employee Assignments"
        unique_together = ('employee', 'stage')
        ordering = ['id']

    def __str__(self):
        return f"{self.employee.name} in {self.stage.name}"

