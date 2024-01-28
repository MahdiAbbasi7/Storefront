
# Project Title

Storefront is a RESTful Store build with Django and Django Rest Framework.


## Installation

Clone the project

```bash
    git clone https://github.com/MahdiAbbasi7/Storefront.git
```
Please activate your virtual environment before running the project and enter the required information, I recommend pipenv.

Now you can run the project
```bash
    docker-compose up -d --build
```
You currently have 7 containers running : 

-    web
-    mariadb
-    smtp4dev
-    redis
-    celery
-    celery-beat
-    flower
-    tests

You access to app from 0.0.0.0:8000
## Features

- Make an order by customers
- Authentication with email using JWT 
- Sending Emails using smtp protocol
- Best performance when handling many requests -(locust)
- Adding new Collection and Products to store by admin
- Automatically remove shopping cart after making order
- Add new items to cart or update quantity of existing item
- Viewing products by customers and add them to their cart
- Ability to view and update user profiles for customers and admins
- Production-ready configuration for Static Files, Database Settings, Gunicorn, Docker

## Technologies used

- Python 3.9 - Programming Language
- Django - Web Framework
- Django Rest Framework - For Building RESTful APIs
- Pytest - Automated Testing
- Docker - Container Platform
- MariaDB - Database
- Git - Version Control System
- Gunicorn - WSGI HTTP Server
- Celery - Task Queue
- Flower - Monitoring Celery Tasks
- Locust - Performance Testing
- Silk - Profiling
- Redis - Caching and Brocker

