FROM python:3.12.3-slim

WORKDIR /app

COPY ../../requirements.txt /app/requirements.txt

RUN apt-get update && apt-get install -y libpq-dev gcc
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY ../../app /app