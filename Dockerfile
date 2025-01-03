# syntax=docker/dockerfile:1
FROM python:3.10-slim
RUN apt-get update && apt-get install -y build-essential postgresql-client libpq-dev
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

#sudo chown -R $USER:$USER .
