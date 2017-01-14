FROM python:3.5
MAINTAINER Konstantin Volodin volodin.konstantin@gmail.com

ADD . /code
WORKDIR /code

COPY ./backend/requirements.txt /
RUN pip install -r /requirements.txt


#CMD ["ls", "-a"]
CMD ["python3", "backend/app.py"]