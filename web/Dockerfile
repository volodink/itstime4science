FROM python:3.5
MAINTAINER Konstantin Volodin volodin.konstantin@gmail.com

COPY ./backend/requirements.txt /
RUN pip install -r /requirements.txt

ADD . /code
WORKDIR /code

CMD ["python3", "-u", "backend/app.py"]
