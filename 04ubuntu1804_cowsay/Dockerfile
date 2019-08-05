FROM ubuntu:18.04

MAINTAINER Eugene Naryshkin <aurcame@gmail.com>

RUN apt-get update && apt install -y cowsay && ln -s /usr/games/cowsay /usr/bin/cowsay

ENTRYPOINT ["cowsay"]

CMD ["Cow says: docker example finished!"]
