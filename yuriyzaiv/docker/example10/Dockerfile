 FROM jenkins/jenkins:lts
 USER root
 
 RUN echo "Add and install all the necessary dependencies"
 RUN apt-get update && \
 apt-get install -qy \
   apt-utils \
   libyaml-dev \
   build-essential \
   python-dev \
   libxml2-dev \
   libxslt-dev \
   libffi-dev \
   libssl-dev \
   default-libmysqlclient-dev \
   python-mysqldb \
   python-pip \
   libjpeg-dev \
   zlib1g-dev \
   libblas-dev\
   liblapack-dev \
   libatlas-base-dev \
   apt-transport-https \
   ca-certificates \
   zip \
   unzip \
   gfortran && \
 rm -rf /var/lib/apt/lists/*
 
 RUN echo "install docker"
 RUN curl -fsSL get.docker.com -o get-docker.sh && sh get-docker.sh
 
 RUN echo "install docker compose"
 RUN curl -L https://github.com/docker/compose/releases/download/1.8.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && \
     chmod +x /usr/local/bin/docker-compose

 RUN echo "===> install pip for python..."  && \ 
     pip install cffi --upgrade && \
     pip install pip2pi ansible==2.0
 
