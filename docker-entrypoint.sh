#!/bin/sh

set -e

cd /jasminwebpanel
ls ./
./manage.py migrate
# RUN ./manage.py createsuperuser
# echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'pass')" | python manage.py shell
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'pass')" | python manage.py shell
./manage.py collectstatic --noinput

exec "$@"
#echo "$1"