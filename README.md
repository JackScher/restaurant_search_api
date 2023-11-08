# Simple Rest API App

1. Run

```bash
python3 -m venv .venv
```

2. Run

```bash
source .venv/bin/activate
```

3. Run

```bash
pip install -r requirements.txt
```

4. Run

```bash
docker compose up -d db
```

5. Run

```bash
python manage.py makemigrations
```

6. Run

```bash
python manage.py migrate
```

7. Run

```bash
python manage.py createsuperuser
```

8. Run

```bash
python manage.py runserver
```

9. To use all methods(GET/POST/PUT/DELETE) you should be logged in. Use admin account you created in the previous step for it. To log in go to '127.0.0.1:8000/admin'.
 
10. .env file example

```
DJANGO_ENV=production
SECRET_KEY=django-insecure-x(%@ol3x1ine89@e(q$$5wb1ew8+0yc-7e+5xtu*%qqqn5v0q1

POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_DB=db
LOCAL_DB_PORT=17550
```
