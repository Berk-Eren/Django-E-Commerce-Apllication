# syntax=docker/dockerfile:1
FROM python:3.10.6
WORKDIR /app/
COPY . .
CMD ["python", "manage.py", "runserver"]