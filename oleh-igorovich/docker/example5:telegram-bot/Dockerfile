FROM python:3.7.4-buster
LABEL Description='Debian10-based develompent environment for creating telegram bots'

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install 

COPY bot/ /src/bot
WORKDIR /src/bot

RUN pip3 install -r /src/bot/requirements.txt