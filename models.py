from django.conf import settings
from django.db import models

class Employee(models.Model):
    SECTOR_CHOICES = [
        ("Sector 1", "Sector 1"),
        ("Sector 2", "Sector 2"),
        ("Sector 3", "Sector 3"),
        ("Sector 4", "Sector 4"),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="employee_profile",
    )
    emp_name = models.CharField(max_length=120)
    emp_id = models.CharField(max_length=50, unique=True)
    role = models.CharField(max_length=100)
    date_of_join = models.DateField()
    branch_sector = models.CharField(max_length=20, choices=SECTOR_CHOICES)
    salary = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return f"{self.emp_id} - {self.emp_name}"
