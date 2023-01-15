"""
Apache Kafka consumer
"""

from kafka3 import KafkaConsumer
from json import loads

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('default',
                         group_id='my-group',
                         bootstrap_servers=['kafka:9092'],
                         auto_offset_reset='earliest',
                         enable_auto_commit=True,
                         value_deserializer=lambda x: loads(x.decode('utf-8'))
                         )

for message in consumer:
    message = message.value
    print('{} consumed'.format(message))