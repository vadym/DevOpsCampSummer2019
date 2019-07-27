FROM centos:7

LABEL version='0.0.1' \
    maintanter='Oleh Kurza'

ENV USER=user \
    PASSWORD=password

RUN useradd ${USER} && yum -y install sudo echo
RUN usermod -aG wheel ${USER} && \
    mkdir -p /home/${USER}
RUN echo ${USER} 'ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers && \ 
    cat /etc/sudoers

USER ${USER}
WORKDIR  /home/${USER}

RUN sudo yum -y install epel-release rpmfusion-free-release \
    yum-utils htop vim iotop \
    cmake gcc-c++ make python3-devel \
    unzip links gpg wget curl

# persistent filesystem
VOLUME /home/${USER}}