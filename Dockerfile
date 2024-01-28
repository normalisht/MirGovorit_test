FROM python:3.11-slim

WORKDIR mir_govorit_app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir
RUN pip install gunicorn==20.1.0

COPY mir_govorit .
COPY .env .

RUN python manage.py migrate
RUN python manage.py  shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')"

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
