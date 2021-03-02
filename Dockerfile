FROM python:3.9

RUN apt-get update

WORKDIR /app

COPY requirements.txt /app/requirements.txt
COPY requirements_dev.txt /app/requirements_dev.txt

RUN pip3 install -r requirements.txt
RUN pip3 install -r requirements_dev.txt
