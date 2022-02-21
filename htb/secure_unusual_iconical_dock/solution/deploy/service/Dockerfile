FROM ubuntu:20.04

# required on our server
ENV http_proxy "http://192.168.2.1:3128"
ENV https_proxy "http://192.168.2.1:3128"

RUN echo 'Acquire::http::proxy "http://192.168.2.1:3128";' >> /etc/apt/apt.conf
RUN echo 'Acquire::https::proxy "http://192.168.2.1:3128";' >> /etc/apt/apt.conf

RUN mkdir /task/

RUN apt update && apt install openssh-server -y
RUN useradd -rm -d /task -s /bin/bash -u 1431 solver
RUN echo 'solver:b6DYaqVcu2' | chpasswd

ADD flag.txt /task/
# make flag unreadable to everyone except root
RUN chmod go-rwx /task/flag.txt
RUN chmod u-w /task/flag.txt
# SUID
RUN chmod +s /usr/bin/file

RUN service ssh start

EXPOSE 21005
CMD ["/usr/sbin/sshd", "-D", "-p 21005"]
