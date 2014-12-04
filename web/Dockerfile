FROM ubuntu:14.04

RUN apt-get update -q && apt-get install -y python python-setuptools
RUN easy_install pip

WORKDIR /app

ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

CMD ["python", "app.py"]
