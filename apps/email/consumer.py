"""
Apache Kafka consumer
"""
import os, django
from kafka3 import KafkaConsumer
from json import loads
from django.core.mail import send_mail

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
django.setup()


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
    print('Recived message {}'.format(message))

    order = loads(message)

    # Admin Email
    send_mail(
        subject='An Order has been completed',
        message='Order #' + str(order["id"]) + 'with a total of $' + str(order["admin_revenue"]) + ' has been completed!',
        from_email='from@email.com',
        recipient_list=['admin@admin.com']
    )

    send_mail(
        subject='An Order has been completed',
        message='You earned $' + str(order["ambassador_revenue"]) + ' from the link #' + order["code"],
        from_email='from@email.com',
        recipient_list=[order["ambassador_email"]]
    )