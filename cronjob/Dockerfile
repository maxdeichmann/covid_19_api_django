FROM python:3
MAINTAINER Maximilian Deichmann <maximiliandeichmann@gmail.com>

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

ENV SOURCE=https://covid.ourworldindata.org/data/full_data.csv
ENV API_HOST=0.0.0.0:8000
ENV POST_PATH=countries/

CMD python cronjob.py
