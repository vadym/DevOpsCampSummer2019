FROM alpine:3.8

MAINTAINER Eugene Naryshkin <aurcame@gmail.com>

RUN apk update && apk add --no-cache mysql-client && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["mysql"]
