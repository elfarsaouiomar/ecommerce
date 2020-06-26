#start config file
# pull official base image
FROM python:3.8.3-alpine

MAINTAINER omarelfarsaoui

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
RUN mkdir /ecommerce_app
WORKDIR /ecommerce_app

COPY ./ecommerceWebSite /ecommerce_app
# install dependencies

COPY ./requirements.txt .
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN apk --update add libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev
RUN pip3 install -r requirements.txt

RUN adduser -D ecommerceuser
USER ecommerceuser

#EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
#CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":8000", "--chdir", "hello", "hello.wsgi:application"]
