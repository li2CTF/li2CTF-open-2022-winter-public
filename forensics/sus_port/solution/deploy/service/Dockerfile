FROM ubuntu:20.04

# required on our server
ENV http_proxy "http://192.168.2.1:3128"
ENV https_proxy "http://192.168.2.1:3128"

RUN echo 'Acquire::http::proxy "http://192.168.2.1:3128";' >> /etc/apt/apt.conf
RUN echo 'Acquire::https::proxy "http://192.168.2.1:3128";' >> /etc/apt/apt.conf

RUN dpkg --add-architecture i386
RUN apt-get update -y
RUN apt-get install -y socat gcc-multilib
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip

RUN mkdir /task/
ADD flag.txt /task/
ADD runner.sh /task/
ADD server.py /task/
ADD requirements.txt /task/
WORKDIR /task/
RUN chmod a+x /usr/bin/python3
RUN chmod a+r /task/flag.txt
RUN chmod +x /task/runner.sh

RUN pip3 install -r requirements.txt

USER nobody
CMD ["./runner.sh"]
