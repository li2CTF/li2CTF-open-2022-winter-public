FROM ubuntu:20.04

# required on our server
ENV http_proxy "http://192.168.2.1:3128"
ENV https_proxy "http://192.168.2.1:3128"

RUN echo 'Acquire::http::proxy "http://192.168.2.1:3128";' >> /etc/apt/apt.conf
RUN echo 'Acquire::https::proxy "http://192.168.2.1:3128";' >> /etc/apt/apt.conf

RUN mkdir /lobby/
RUN mkdir /books/

RUN apt-get update && apt-get install openssh-server sudo -y
RUN apt-get install python3 python3-pip -y

ADD books/* /books/
ADD order_book.py /usr/local/share/
ADD order_book /usr/bin/

ADD add_visitors.sh /
ADD visitors.txt /
RUN ./add_visitors.sh
RUN rm visitors.txt
RUN rm add_visitors.sh
RUN rm /usr/bin/wget

RUN chmod go-rwx /books/*
RUN chmod u-w /books/*
RUN chmod go-w /usr/local/share/order_book.py
RUN chmod go+x /usr/local/share/order_book.py
RUN chmod go-w /usr/bin/order_book
RUN chmod +s /usr/bin/order_book

# prevent flagsharing
RUN chmod go-rwx /usr/bin/chmod

RUN service ssh start

EXPOSE 21009
CMD ["/usr/sbin/sshd", "-D", "-p 21009"]
