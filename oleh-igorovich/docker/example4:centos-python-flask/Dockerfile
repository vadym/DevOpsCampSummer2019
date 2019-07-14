FROM centos:7.6.1810
LABEL Description='Hello-world Flask application, based on Python 3.6 and CentOS 7.6 image'

# Installing IUS repo
RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm && yum -y update
# Installing python 3.6
RUN yum install -y \
 gcc \ 
 libffi-devel \
 libevent-dev \
 openssl-devel \ 
 python36u \
 python36u-libs \
 python36u-devel \
 python36-pip

# Copying folder from current dir, assigning working dir
COPY app/ /src/app
WORKDIR /src/app

# Installing Flask and its dependencies based on requirements.txt
RUN pip3 install -r /src/app/requirements.txt
EXPOSE 5000

# Setting up locale
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8     

CMD flask run --host=0.0.0.0

