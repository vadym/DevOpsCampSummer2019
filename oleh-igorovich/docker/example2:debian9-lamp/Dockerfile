FROM debian:stretch
LABEL Description='LAMP stack based on Debian Stretch, latest MariaDB and PHP 7.3'

# adding apt-repositories
RUN apt update \
 && apt -y install lsb-release apt-transport-https ca-certificates wget\
 && wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg \
 && echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" | tee /etc/apt/sources.list.d/php7.3.list
RUN apt update

# installing LAMP + PHP modules
RUN apt install -y \
 apache2 \
 apache2-utils \
 mariadb-server \
 mariadb-client \
 libapache2-mod-php7.3 \
 libapache2-mod-php \
 php7.3 \
 php7.3-cli \
 php7.3-fpm \
 php7.3-json \
 php7.3-pdo \
 php7.3-mysql \
 php7.3-zip \
 php7.3-gd \
 php7.3-mbstring \
 php7.3-curl \
 php7.3-xml \
 php7.3-bcmath \
 php7.3-json

# Enable php as Apache module
RUN a2enmod php7.3

# Opening ports for Apache and MySQL
EXPOSE 80
EXPOSE 3306

RUN echo "Please finish mysql setup by running 'mysql_secure_installation'"
CMD bash
