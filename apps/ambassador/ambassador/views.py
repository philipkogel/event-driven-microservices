"""Views for ambassador API"""

from rest_framework import views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from json import dumps
from kafka3 import KafkaProducer
import requests

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


class CreateView(views.APIView):
  """Register Ambasador View"""

  def post(self, request):
    """Register ambasador"""
    data = request.data
    data['is_ambassador'] = 'api/ambasadaor' in request.path

    response = requests.post('http://host.docker.internal:8003/api/user/create/', data)

    return Response(response.json())


class LoginView(views.APIView):
  def post(self, request):
    data = request.data
    data['scope'] = 'ambasador' if 'api/amabasador' in request.path else 'admin'


    res = requests.post('http://host.docker.internal:8003/api/user/login/', data).json()

    response = Response()
    response.set_cookie(key='jwt', value=res['jwt'], httponly=True)
    response.data = {
      'message': 'success',
    }

    return response