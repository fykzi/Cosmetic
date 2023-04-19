FROM python:3.10.10

SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir cosmetic
WORKDIR /cosmetic/

ADD . /cosmetic/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD gunicorn Cosmetic.wsgi:application -b 0.0.0.0:8000