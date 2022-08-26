# syntax=docker/dockerfile:1
FROM python:3.10.6
WORKDIR /app/

RUN apt-get update && apt-get install nginx vim -y --no-install-recommends

COPY Pipfile /app/Pipfile
COPY Pipfile.lock /app/Pipfile.lock

RUN pip install pipenv
RUN pipenv shell

RUN python manage.py makemigrations orders
RUN python manage.py makemigrations products
RUN python manage.py makemigrations users

RUN python manage.py migrate

EXPOSE 8000
CMD ["python", "manage.py", "runserver"]