FROM alpine:latest

RUN apk add build-base socat

RUN mkdir -p /app
WORKDIR /app

COPY src src
COPY Makefile Makefile
RUN make

RUN rm -rf ./src ./Makefile

WORKDIR /app/build

ENTRYPOINT socat TCP4-LISTEN:1337,reuseaddr,fork EXEC:./vuln,stderr

EXPOSE 1337
