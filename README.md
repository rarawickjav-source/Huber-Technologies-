# Huber Technologies Employee Portal

Stack:
- Django
- PostgreSQL
- Django REST Framework
- JWT authentication
- Bootstrap

## VS Code setup

1. Extract the ZIP.
2. Open the extracted folder in VS Code.
3. Create and activate a virtual environment.
4. Install requirements.
5. Create PostgreSQL database `huber_emp_db`.
6. Edit `config/settings.py` and replace `YOUR_POSTGRES_PASSWORD`.
7. Run migrations.
8. Create a superuser.
9. Run the server.

Windows:
```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## URLs

Website: http://127.0.0.1:8000/
Signup: http://127.0.0.1:8000/signup/
Login: http://127.0.0.1:8000/login/
Admin: http://127.0.0.1:8000/admin/
API: http://127.0.0.1:8000/api/employees/
JWT: http://127.0.0.1:8000/api/token/

## End-to-end validation

1. Home page loads.
2. Signup with valid data.
3. Confirm "Sign Up Completed".
4. Open admin and confirm employee exists.
5. Login with the same email/password.
6. Confirm "Login Successful".
7. Click Continue and verify employee data.
8. Test invalid password and duplicate email/employee ID.
9. Test salary with decimal/non-number input.
10. Obtain JWT from `/api/token/`.
11. Call `/api/employees/` with `Authorization: Bearer <access-token>`.
12. Call `/api/employees/` without token and confirm it is rejected.

## Important

Do not commit real PostgreSQL passwords or Django secret keys to Git.
