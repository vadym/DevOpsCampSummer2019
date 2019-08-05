FROM alpine:latest

MAINTAINER Eugene Naryshkin aurcame@gmail.com

RUN apk add --update nginx && mkdir /tmp/nginx && rm -rf /var/cache/apk/*

EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"]
