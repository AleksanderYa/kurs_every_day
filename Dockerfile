# syntax=docker/dockerfile:1

FROM python:3.8

ENV PYTHONUNBUFFERED=1

RUN mkdir usr/DockerTest

RUN ls

RUN cd usr/DockerTest/

RUN ls

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

WORKDIR T/

EXPOSE 80:8000

RUN ls