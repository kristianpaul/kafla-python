from klein import run, route
import json

from kafka import KafkaProducer
from kafka.errors import KafkaError


@route('/', methods=['POST'])
def do_post(request):
    #content = json.loads(request.content.read())
    #response = json.dumps(dict(the_data=content), indent=4)

    producer = KafkaProducer(bootstrap_servers=['kafla:9092'])
    producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('ascii'))
    producer.send('my-topic', request.content.read())
    producer.flush()
    producer = KafkaProducer(retries=5)

    return response

@route('/')
def hello(request):
    return "Hello, world!"

run("0.0.0.0", 8080)
