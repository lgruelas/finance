FROM python:3.7

WORKDIR /usr/src/requirements

COPY requirements.txt /usr/src/requirements

COPY wait-for-it.sh /usr/src/requirements

COPY ../.git /.git

RUN pip install -r requirements.txt && chmod +x wait-for-it.sh

WORKDIR /usr/src/finance