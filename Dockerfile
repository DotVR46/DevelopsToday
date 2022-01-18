# pull official base image
FROM python:3.9-alpine
# set work directory
WORKDIR D:/PyCharm_projects/DevelopsToday
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
# copy project
COPY . .

CMD gunicorn core.wsgi:application --bind 0.0.0.0:$PORT