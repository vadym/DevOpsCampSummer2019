FROM alpine:3.9

MAINTAINER Eugene Naryshkin <aurcame@gmail.com>

RUN apk update && apk add --no-cache mysql-client && rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["mysql"]
