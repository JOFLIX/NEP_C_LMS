release: python manage.py migrate
release: python manage.py syncdb
web: gunicorn project.wsgi --log-file -