"""Views for ambassador API"""

from rest_framework.decorators import api_view
from rest_framework.response import Response
from json import dumps
from kafka3 import KafkaProducer

@api_view(['POST'])
def confirm(request):
    """Returns successful confirm."""
    producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))
    if producer is not None:
      data = {'number' : 100}
      producer.send('default', value=data)
    return Response({'number': data["number"]})