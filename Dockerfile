FROM python:3.10-alpine

EXPOSE 8000

RUN apk add --no-cache gcc python3-dev musl-dev mariadb-connector-c-dev

ADD . /django_ec2

WORKDIR /django_ec2

RUN pip install mysqlclient  

RUN pip install --upgrade setuptools

RUN pip install -r requirements.txt

RUN python manage.py makemigrations

RUN python manage.py migrate

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]