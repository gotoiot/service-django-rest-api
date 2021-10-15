# pull the official base image
FROM python:3.8

RUN useradd -ms /bin/bash gotoiot

# set work directory
RUN mkdir /app
ADD requirements.txt /app
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH $PYTHONPATH:/app

# install dependencies
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

STOPSIGNAL SIGHUP

# Copy all code files into image. Uncomment for production
ADD . /app

EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD su gotoiot -c 'python manage.py runserver 0.0.0.0:8000'
