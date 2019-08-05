FROM debian:jessie

RUN apt-get update && apt-get install -y \
      build-essential \
      zlib1g-dev \
      libssl-dev \
      libreadline6-dev \
      libyaml-dev

ADD http://cache.ruby-lang.org/pub/ruby/2.1/ruby-2.1.1.tar.gz /tmp/
RUN cd /tmp && \
      tar -xzf ruby-2.1.1.tar.gz && \
      cd ruby-2.1.1 && \
      ./configure && \
      make && \
      make install && \
      cd .. && \
      rm -rf ruby-2.1.1 && \
      rm -f ruby-2.1.1.tar.gz
