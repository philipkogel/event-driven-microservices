from time import sleep
from json import dumps
from kafka3 import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

for e in range(10):
    data = {'number' : e}
    producer.send('default', value=data)
    sleep(5)