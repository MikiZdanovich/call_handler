FROM python:3-slim

MAINTAINER MikiZdanovich

ENV PYTHONDONTWRITEBYTECODE 1
ENV FLASK_APP "manage.py"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True

WORKDIR /app

RUN pip install --upgrade pip
COPY ./requirenments.txt /app/requirements.txt
RUN pip install -r requirements.txt

ADD . /app/

CMD python "app/service/data_monitoring.py"


