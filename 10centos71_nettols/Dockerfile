FROM centos

MAINTAINER Eugene Naryshkin <aurcame@gmail.com>

RUN yum install -y net-tools 
RUN yum install -y telnet

ENTRYPOINT ["telnet"]

CMD ["telnet 192.168.1.1 22"]
