# Run collect static and migrations
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py createsuperuser --username admin --email admin@example.com --password admin

