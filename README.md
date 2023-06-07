# django-turingquant
site com as funcoes da biblioteca turingquant

### Tutorial w3s:
https://www.w3schools.com/django/django_urls.php

## 1. criar ambiente virtual

## 2. criar projeto
```
django-admin startproject turingquant
```

## 3. criar app
```

```

## 4. inserir app em settings.py

```
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "risco_retorno"
]
```

## 5. Instalar bibliotecas
```
pip install yfinance
pip install 
```

# 6. Modificar os dois arquivos: urls.py. O da app e o do projeto

## commandos do django:

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## caso dê algum problema com o port, matamos o processo do port 8000:
```
kill -9 $(lsof -ti:8000)
```
