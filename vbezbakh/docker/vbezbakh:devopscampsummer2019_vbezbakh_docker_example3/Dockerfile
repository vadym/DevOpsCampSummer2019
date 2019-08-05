FROM ubuntu
RUN apt-get update
RUN apt-get -y install sl
RUN ln -s /usr/games/sl /usr/bin/sl
ENTRYPOINT ["sl", "-l"]
