FROM python:3.7

WORKDIR /usr/src/finance

COPY requirements.txt /usr/src/finance

COPY wait-for-it.sh /usr/src/finance

RUN pip install -r requirements.txt && chmod +x wait-for-it.sh

COPY . /usr/src/finance