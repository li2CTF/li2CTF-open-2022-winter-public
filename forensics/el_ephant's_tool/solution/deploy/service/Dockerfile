FROM ubuntu:20.04

ENV PYTHONUNBUFFERED 1

# required on our server
ENV http_proxy "http://192.168.2.1:3128"
ENV https_proxy "http://192.168.2.1:3128"
ENV HTTP_PROXY "http://192.168.2.1:3128"
ENV HTTPS_PROXY "http://192.168.2.1:3128"

RUN echo 'Acquire::http::proxy "http://192.168.2.1:3128";' >> /etc/apt/apt.conf
RUN echo 'Acquire::https::proxy "http://192.168.2.1:3128";' >> /etc/apt/apt.conf

# prevent some shitty thing from dialog duirng image building
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update -y
RUN dpkg --add-architecture i386
RUN apt-get install php -y
RUN apt-get install python3 python3-pip -y
RUN apt-get install curl -y

RUN mkdir /task
RUN mkdir /ttt
WORKDIR /task/

ADD flag.txt /task/
ADD requirements.txt /task/
ADD bot.py /task/
ADD TOKEN /ttt/

RUN useradd -rm -d "/task/" -s /bin/bash -u 12345 "elephant"
RUN echo "elephant:hCqx7zA1vHdBx3jYz" | chpasswd
RUN chown "root:root" "/task/"
RUN chown "elephant:elephant" "/ttt/TOKEN"
RUN chown "elephant:elephant" "/ttt"

RUN chmod a+rwx /ttt/TOKEN

RUN chmod a+r /task/flag.txt

RUN pip3 install -r requirements.txt

USER elephant
CMD ["python3", "bot.py"]
