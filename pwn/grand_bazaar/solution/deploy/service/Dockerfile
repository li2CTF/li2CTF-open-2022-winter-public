FROM ubuntu:20.04

# required on our server
ENV http_proxy "http://192.168.2.1:3128"
ENV https_proxy "http://192.168.2.1:3128"

RUN echo 'Acquire::http::proxy "http://192.168.2.1:3128";' >> /etc/apt/apt.conf
RUN echo 'Acquire::https::proxy "http://192.168.2.1:3128";' >> /etc/apt/apt.conf

RUN dpkg --add-architecture i386
RUN apt-get update -y
RUN apt-get install -y socat gcc-multilib

RUN mkdir /task/
ADD book /task/
ADD lamp /task/
ADD shoes /task/
ADD flag /task/
ADD task.elf /task/
WORKDIR /task/
RUN chmod a+x /task/task.elf
RUN chmod a+r /task/flag

USER nobody
CMD ["socat", "TCP-LISTEN:21016,reuseaddr,fork", "EXEC:/task/task.elf"]
