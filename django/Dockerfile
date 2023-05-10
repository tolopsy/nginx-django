FROM python:3.9-alpine
RUN apk add -u gcc musl-dev

WORKDIR /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./staticfiles/ ./staticfiles/
