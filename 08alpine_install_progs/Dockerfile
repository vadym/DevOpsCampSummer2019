FROM alpine:3.4

MAINTAINER Eugene Naryshkin <aurcame@gmail.com>

RUN apk update && \
    apk add curl && \
    apk add vim && \
    apk add git
RUN echo -e "\n\ncurl + vim + git installed on " && cat /proc/version && echo -e "\n\n"
