FROM ubuntu:19.04
RUN apt-get install -y python3
RUN apt-get install -y python3-pip

RUN ln -s /usr/bin/python3 /usr/bin/python
RUN ln -s /usr/bin/pip3 /usr/bin/pip

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install cloudmesh-installer
RUN mkdir cm

WORKDIR cm

CMD [ "python", "server.py" ]
