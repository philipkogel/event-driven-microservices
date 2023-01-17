from json import dumps
from kafka3 import KafkaProducer

producer: KafkaProducer or None = None

def confirm_order(data):
     global producer
     if producer is None:
          producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))
     producer.send('default', value=data)