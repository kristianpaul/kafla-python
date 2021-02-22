#!/bin/bash

cd /kafka_2.13-2.7.0
sed -i 's/localhost:2181/zookeeper:2181/g' config/server.properties
sed -i 's|#listeners=PLAINTEXT://:9092|listeners=PLAINTEXT://kafla:9092|g' config/server.properties
#sed -i 's|#advertised.listeners=PLAINTEXT://your.host.name:9092|advertised.listeners=PLAINTEXT://kafla:9092|g' config/server.properties
./bin/kafka-server-start.sh config/server.properties
