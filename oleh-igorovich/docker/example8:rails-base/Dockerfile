FROM ruby:2.6.3-buster

RUN apt-get update -qq && apt-get install -y build-essential \
    libpq-dev \
    libxml2-dev \ 
    libxslt1-dev \
    libqt4-dev \
    xvfb \
    nodejs

ENV APP_HOME /myapp
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

ADD Gemfile* $APP_HOME/
RUN bundle install

ADD . $APP_HOME