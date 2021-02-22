FROM ubuntu:20.04

RUN  set -x \
    && apt-get update && apt-get install -y python3 python3-pip python3-twisted \
    && pip3 install klein kafka-python

COPY run.sh /run.sh
COPY api.py /api.py

EXPOSE 8080

CMD  /bin/sh /run.sh
