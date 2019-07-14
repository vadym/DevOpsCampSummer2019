FROM alpine
RUN apk update && apk add python3
COPY . /app
WORKDIR /app
CMD ["python3","rps.py"]
