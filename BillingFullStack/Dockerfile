FROM python:3.10

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /home/app/billing

WORKDIR /home/app/billing

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install psycopg2==2.9.7

COPY . .
