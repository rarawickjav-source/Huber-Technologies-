from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    mail = serializers.EmailField(source="user.email", read_only=True)

    class Meta:
        model = Employee
        fields = [
            "id", "emp_name", "emp_id", "role", "date_of_join",
            "branch_sector", "salary", "mail", "created_at",
        ]
        read_only_fields = ["id", "created_at", "mail"]
