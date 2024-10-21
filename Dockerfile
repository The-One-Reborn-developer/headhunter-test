FROM python:3.12-slim

WORKDIR /

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

ENV PYTHONPATH=/app

CMD ["python3", "/app/api/flask_app.py"]