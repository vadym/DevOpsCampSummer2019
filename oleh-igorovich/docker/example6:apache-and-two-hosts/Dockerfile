FROM centos:7.6.1810

RUN yum -y update
RUN yum -y install \
    curl \
    httpd \
    wget 

ENV VHOST1=example-one.com
ENV VHOST2=example-two.com

RUN mkdir -p /var/www/${VHOST1}/public_html \
    /var/www/${VHOST2}/public_html

COPY ./src/index.html /var/www/${VHOST1}/public_html/
COPY ./src/index.html /var/www/${VHOST2}/public_html/

RUN mkdir -p /etc/httpd/sites-available \
    /etc/httpd/sites-enabled 

COPY ./src/vhost.d /etc/httpd/sites-available/${VHOST1}.conf
COPY ./src/vhost.d /etc/httpd/sites-available/${VHOST2}.conf

RUN chmod -R 755 /var/www

RUN echo 'IncludeOptional sites-enabled/*.conf' >> /etc/httpd/conf/httpd.conf

RUN sed -i -e 's/example.com/${VHOST1}/g' /etc/httpd/sites-available/${VHOST1}.conf && \
    sed -i -e 's/example.com/${VHOST2}/g' /etc/httpd/sites-available/${VHOST2}.conf

RUN ln -s /etc/httpd/sites-available/${VHOST1}.conf /etc/httpd/sites-enabled/${VHOST1}.conf && \
    ln -s /etc/httpd/sites-available/${VHOST2}.conf /etc/httpd/sites-enabled/${VHOST2}.conf

RUN echo 'hello from ' ${VHOST1} >> /var/www/${VHOST1}/public_html/index.html && \
    echo 'hello from ' ${VHOST2} >> /var/www/${VHOST2}/public_html/index.html

EXPOSE 80

CMD /usr/sbin/httpd -D FOREGROUND