#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

echo "creating suuuuuuuuper user"
python manage.py createsuperuser --username admin --email admin@example.com --password admin
# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000
