FROM ubuntu:latest

RUN apt-get update
RUN apt-get install gcc make ruby ruby-dev -y
RUN gem install fluentd
RUN gem install fluent-plugin-mongo 
RUN mkdir /log
RUN mkdir /td-agent
COPY fluent.conf /
WORKDIR /
CMD ["fluentd","-c","fluent.conf"]
