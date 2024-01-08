FROM python:3.9

ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Required to install mysqlclient with Pip
RUN apt-get update \
  && apt-get install python3-dev default-libmysqlclient-dev gcc -y

# Install pipenv
RUN pip install --upgrade pip 
RUN pip install pipenv

# Install application dependencies
COPY Pipfile Pipfile.lock /app/
# We use the --system flag so packages are installed into the system python
# and not into a virtualenv. Docker containers don't need virtual environments. 
RUN pipenv install --system --dev

# Copy the application files into the image
COPY . /app/

# Expose port 8000 on the container
EXPOSE 8000
# start server  
CMD docker run -p 8000:8000 --restart on-failure -v .:/app ./wait-for-it.sh mariadb:3306 -- ./docker-entrypoint.sh
CMD docker run -p 3307:3306 --restart always -e MARIADB_DATABASE=storefront2 -e MARIADB_ROOT_PASSWORD=1 -e MARIADB_USER=root -v mysqldata:/var/lib/mysql mariadb:10.6.12
CMD docker run -p 6379:6379 --restart always -v redisdata:/data redis:6.2-alpine
CMD docker run -p 5000:80 -p 2525:25 --restart always rnwood/smtp4dev:v3
CMD docker run -v .:/app celery -A storefront worker --loglevel=info
CMD docker run -v .:/app celery -A storefront beat --loglevel=info
CMD docker run -e DEBUG=1 -e CELERY_BROKER=redis://redis:6379/0 -e CELERY_BACKEND=redis://redis:6379/0 -p 5555:5555 celery -A storefront flower
CMD docker run -t -v .:/app ./wait-for-it.sh mariadb:3306 -- ptw
