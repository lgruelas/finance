FROM python:3.7-slim

WORKDIR /usr/src/finance

COPY requirements.txt /usr/src/finance

RUN pip install -r requirements.txt

COPY . /usr/src/finance

CMD ["python", "manage.py run --settings=backend.settings.dev"]