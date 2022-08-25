# syntax=docker/dockerfile:1
FROM python:3.10.6
WORKDIR /app/
COPY . .
RUN pip install pipenv
RUN pipenv shell
CMD ["python", "manage.py", "runserver"]