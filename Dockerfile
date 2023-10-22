FROM python:3.11

WORKDIR /config

COPY ./requirements.txt /config/

RUN pip install -r /config/requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]