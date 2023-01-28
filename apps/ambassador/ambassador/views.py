"""Views for ambassador API"""

from rest_framework import views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from json import dumps
from kafka3 import KafkaProducer
from ambassador.services import UserService

@api_view(['POST'])
def confirm(request):
    """Returns successful confirm via kafka."""
    producer = KafkaProducer(bootstrap_servers=['kafka:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))
    if producer is not None:
      data = {'number' : 100}
      producer.send('default', value=data)
    return Response({'number': data["number"]})


class CreateView(views.APIView):
  """Register Ambassador View"""

  def post(self, request):
    """Register ambassador"""
    data = request.data
    data['is_ambassador'] = True

    return Response(UserService.post('', data=data, is_users_endpoint=True))


class LoginView(views.APIView):
  def post(self, request):
    data = request.data
    data['scope'] = 'ambassador'

    res = UserService.post('login', data=data)

    response = Response()
    response.set_cookie(key='jwt', value=res['jwt'], httponly=True)
    response.data = {
      'message': 'success',
    }

    return response

class LogoutView(views.APIView):
  """Logout Ambassador View"""
  def post(self, request):
    """Logout endpoint."""
    UserService.post('logout', headers=request.headers)

    response = Response()
    response.delete_cookie(key='jwt')
    response.data = {
      'message': 'success',
    }

    return response

class UserView(views.APIView):
    """Retrive and return user."""

    def get(self, request):
      """Return user from internal User API."""
      return Response(request.user_ms)

    def put(self, request, pk=None):
      """User profile info update"""
      return Response(UserService.put('', data=request.data, headers=request.headers))


class ProfilePasswordView(views.APIView):
  """Manage profile view."""

  def put(self, request, pk=None):
    """User profile info update"""
    return Response(UserService.put('password', data=request.data, headers=request.headers))


class AmbassadorView(views.APIView):
    """Manage ambassadors (Users)"""
    def get(self, request):
      """Return all ambassadors."""
      ambassadors = UserService.get(
        '',
        params='?is_ambassador=true',
        headers=request.headers,
        is_users_endpoint=True
      )
      return Response(ambassadors)
