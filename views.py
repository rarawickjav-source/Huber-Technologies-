from datetime import date
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import redirect, render
from .models import Employee

def home(request):
    return render(request, "home.html")

def signup(request):
    if request.method == "POST":
        emp_name = request.POST.get("emp_name", "").strip()
        emp_id = request.POST.get("emp_id", "").strip()
        role = request.POST.get("role", "").strip()
        date_of_join = request.POST.get("date_of_join", "").strip()
        branch_sector = request.POST.get("branch_sector", "").strip()
        salary = request.POST.get("salary", "").strip()
        mail = request.POST.get("mail", "").strip().lower()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")
        errors = []

        if not all([emp_name, emp_id, role, date_of_join, branch_sector, salary, mail, password, confirm_password]):
            errors.append("All fields are required.")

        if emp_name and not emp_name.replace(" ", "").isalpha():
            errors.append("Employee name must contain letters only.")

        if Employee.objects.filter(emp_id__iexact=emp_id).exists():
            errors.append("Employee ID already exists.")

        if User.objects.filter(email__iexact=mail).exists():
            errors.append("Email is already registered.")

        try:
            join_date = date.fromisoformat(date_of_join)
            if join_date > date.today():
                errors.append("Date of joining cannot be in the future.")
        except ValueError:
            errors.append("Enter a valid joining date.")

        try:
            salary_value = int(salary)
            if salary_value < 0:
                errors.append("Salary cannot be negative.")
        except ValueError:
            errors.append("Salary must contain integer values only.")
            salary_value = 0

        if branch_sector not in dict(Employee.SECTOR_CHOICES):
            errors.append("Choose a valid sector.")

        if len(password) < 8:
            errors.append("Password must contain at least 8 characters.")

        if password != confirm_password:
            errors.append("Password and Confirm Password must match.")

        if errors:
            for error in errors:
                messages.error(request, error)
            return render(request, "signup.html", {"form_data": request.POST})

        with transaction.atomic():
            user = User.objects.create_user(
                username=mail, email=mail, password=password, first_name=emp_name
            )
            Employee.objects.create(
                user=user, emp_name=emp_name, emp_id=emp_id, role=role,
                date_of_join=join_date, branch_sector=branch_sector,
                salary=salary_value,
            )

        return render(request, "signup.html", {"success": True})

    return render(request, "signup.html")

def login_view(request):
    if request.method == "POST":
        mail = request.POST.get("mail", "").strip().lower()
        password = request.POST.get("password", "")
        user = authenticate(request, username=mail, password=password)

        if user is not None:
            login(request, user)
            employee = getattr(user, "employee_profile", None)
            if employee is None:
                messages.error(request, "This account is not linked to an employee profile.")
                return redirect("login")
            return render(request, "login.html", {"success": True, "employee": employee})

        messages.error(request, "Invalid employee mail or password.")

    return render(request, "login.html")

def welcome(request):
    if not request.user.is_authenticated:
        return redirect("login")
    employee = getattr(request.user, "employee_profile", None)
    if employee is None:
        messages.error(request, "Employee profile not found.")
        return redirect("login")
    return render(request, "welcome.html", {"employee": employee})
