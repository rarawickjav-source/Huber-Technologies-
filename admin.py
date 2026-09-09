from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "emp_id", "emp_name", "role", "branch_sector",
        "salary", "get_email", "date_of_join", "created_at",
    )
    search_fields = ("emp_id", "emp_name", "role", "user__email")
    list_filter = ("branch_sector", "role", "date_of_join")
    readonly_fields = ("created_at",)
    ordering = ("-created_at",)

    @admin.display(description="Email")
    def get_email(self, obj):
        return obj.user.email
