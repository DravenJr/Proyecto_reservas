FROM python:3.11-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

#Copiar todo el código del proyecto
COPY . /app

#Evitar buffering de logs
ENV PYTHONUNBUFFERED=1

#Ejecutar migraciones y luego levantar Gunicorn
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]


