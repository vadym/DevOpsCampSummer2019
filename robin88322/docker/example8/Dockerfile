FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
    aufs-tools \
    automake \
    build-essential \
    dpkg-sig \
    libcap-dev \
    libsqlite3-dev \
    reprepro \
    wget\
 && rm -rf /var/lib/apt/lists/*

RUN wget -O - https://github.com | wc -l > /number && cat /number
