from kafka import KafkaConsumer

print ("Starting...")
consumer = KafkaConsumer('my-topic',
                         group_id='my-group',
                         bootstrap_servers=['kafla:9092'])
print ("Waiting...")
while True:
    for message in consumer:
        print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                              message.offset, message.key,
                                              message.value))
