FROM centos

ENV PASSWORD=password
ENV USER=user

RUN yum -y install openssh-server

RUN useradd ${USER} && \
    echo ${PASSWORD}} | passwd ${USER} --stdin && \
    mkdir -p /home/${USER}/.ssh/authorized_keys && \
    chmod 700 /home/${USER}/.ssh

RUN chown ${USER}:${USER}   -R /home/${USER} && \
    chmod 600 /home/${USER}/.ssh/authorized_keys

RUN /usr/sbin/sshd-keygen

CMD /usr/sbin/sshd -D