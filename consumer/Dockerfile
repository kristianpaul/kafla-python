FROM ubuntu:20.04

RUN set -x \
    && apt-get update  && apt-get -y install httpie python3-pip ncat vim\
    && pip3 install kafka-python


COPY run.sh /run.sh
COPY consumer.py /consumer.py

CMD /bin/sh /run.sh
