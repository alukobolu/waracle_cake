
# syntax=docker/dockerfile:1

FROM python:3.11.5

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN python manage.py migrate

RUN python manage.py test

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]