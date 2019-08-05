FROM alpine:3.8

MAINTAINER Eugene Naryshkin <aurcame@gmail.com>

RUN apk --update add sudo                                     && \
    \
    \
    echo "01 Install Python runtime\n"  && \
    apk --update add python py-pip openssl ca-certificates    && \
    apk --update add --virtual build-dependencies \
                python-dev libffi-dev openssl-dev build-base  && \
    pip install --upgrade pip cffi                            && \
    \
    \
    echo "02 Install Ansible\n"        && \
    pip install ansible                && \
    \
    \
    echo "03 Clean up package list\n"     && \
    apk del build-dependencies            && \
    rm -rf /var/cache/apk/*               && \
    \
    \
    echo "04 Add hosts for convenience\n"  && \
    mkdir -p /etc/ansible                        && \
    echo 'localhost' > /etc/ansible/hosts

ENTRYPOINT [ "ansible-playbook", "--version" ]
