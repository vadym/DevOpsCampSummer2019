FROM ubuntu

RUN apt-get update && apt-get install -y fortune && ln -s /usr/games/fortune /usr/bin/fortune

ENTRYPOINT ["fortune"]
