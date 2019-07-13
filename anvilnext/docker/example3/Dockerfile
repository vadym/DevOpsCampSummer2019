ARG BASE_IMAGE
FROM ${BASE_IMAGE}
LABEL maintainer="anvilnext's image of alpine & Java"

FROM openjdk:8-jre as builder
EXPOSE 4040
ENTRYPOINT ["java", "-jar"]
CMD ["/simple.jar"]

FROM maven:3.3-jdk-8
COPY --from=builder /build/target/demoapp.jar /opt/
WORKDIR /build
RUN mvn clean install
ENTRYPOINT ["java", "-jar", "/opt/demoapp.jar"]
