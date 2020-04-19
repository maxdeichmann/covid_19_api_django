FROM python:3
MAINTAINER Maximilian Deichmann <maximiliandeichmann@gmail.com>

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

ENV PROJECT_ROOT /code
WORKDIR $PROJECT_ROOT

CMD python manage.py runserver 0.0.0.0:8000
#ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]