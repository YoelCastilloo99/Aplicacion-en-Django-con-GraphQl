release: python manage.py migrate --noinput
web: gunicorn mysitio.wsgi:application --log-file -