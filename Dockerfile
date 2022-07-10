FROM python:3.9-slim-buster

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential libpq-dev \
    unixodbc-dev \
    unixodbc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0
ENV PORT=8000

RUN python -m pip install --upgrade pip

ADD ./requirements.txt /app/requirements.txt

RUN pip install  --no-cache-dir -r requirements.txt
COPY . .


RUN python manage.py collectstatic --noinput


# RUN addgroup app && adduser -S -G app app 
# USER app

CMD gunicorn RideManagement.wsgi:application --bind 0.0.0.0:$PORT  --timeout 600
