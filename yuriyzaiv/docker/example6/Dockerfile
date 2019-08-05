FROM ubuntu

RUN apt-get update &&  apt-get install libaa-bin -y && apt-get install caca-utils -y && ln -s /usr/games/caca-utils /usr/bin/caca-utils

ENTRYPOINT ["aafire"]
