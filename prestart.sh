# Run collect static and migrations
echo "creating suuuuuuuuper user"
python manage.py createsuperuser --username admin --email admin@example.com --password admin
python manage.py collectstatic --noinput
python manage.py migrate


