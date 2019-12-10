FROM ubuntu:19.04

RUN apt-get update

RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install -y python3
RUN apt-get install -y python3-pip

RUN ln -s /usr/bin/python3 /usr/bin/python
RUN ln -s /usr/bin/pip3 /usr/bin/pip

RUN mkdir cm
WORKDIR /cm


RUN pip install -r requirements.txt

RUN pip install cloudmesh-installer

COPY /cm/aws/
CMD [ "python", "server.py" ]
