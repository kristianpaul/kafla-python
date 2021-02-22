FROM ubuntu:20.04

RUN set -x \
    && apt-get update  && apt-get -y install wget openjdk-13-jdk \
    && wget https://downloads.apache.org/kafka/2.7.0/kafka_2.13-2.7.0.tgz \
    && tar -xzf kafka_2.13-2.7.0.tgz \
    && cd kafka_2.13-2.7.0

COPY run.sh /run.sh

EXPOSE 44121

CMD /bin/sh /run.sh
