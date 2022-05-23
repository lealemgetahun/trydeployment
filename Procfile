release: python manage makemigrations  api
release: python manage.py migrate

web: gunicorn apiproject.wsgi.py