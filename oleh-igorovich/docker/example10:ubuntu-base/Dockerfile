FROM ubuntu:18.04

LABEL version="0.0.1"
# change it
ENV USER=user \
    PASSWORD=password  
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y sudo software-properties-common

RUN useradd ${USER} 
RUN usermod -aG sudo ${USER} && \
    mkdir -p /home/${USER}
RUN echo ${USER} 'ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers && \ 
    cat /etc/sudoers

USER ${USER}
WORKDIR  /home/${USER}

RUN sudo add-apt-repository ppa:webupd8team/java && \
    sudo apt-get update
RUN sudo apt-get install -y vim htop iotop wget curl bash-completion \
    cmake gcc make unzip links gpg wget curl
    
# persistent filesystem
VOLUME /home/${USER}}