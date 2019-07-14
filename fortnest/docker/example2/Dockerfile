FROM debian:latest
RUN apt-get update && apt-get install -y maven git

ENV CLONE_DIR="/root/" \
    COMPILE_DIR="/root/java-WebServer/"

WORKDIR ${CLONE_DIR}
RUN git clone https://github.com/dasanjos/java-WebServer.git

WORKDIR ${COMPILE_DIR}
RUN mvn clean package

EXPOSE 80

CMD ["/usr/bin/java", "-jar", "/root/java-WebServer/target/java-WebServer-0.1-jar-with-dependencies.jar", "80"]
