FROM debian:jessie

MAINTAINER Eugene Naryshkin aurcame@gmail.com

RUN apt-get update && apt-get install -y \
      wget \
      build-essential

RUN wget http://download.redis.io/redis-stable.tar.gz

RUN tar xvzf redis-stable.tar.gz
