"""Views for User API."""

from rest_framework import generics, views
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from user.serializers import UserSerializer
from core.models import User
from user.authentication import JWTAuthentication


class CreateUserView(generics.CreateAPIView):
  """Create a new user in the system."""
  serializer_class = UserSerializer


class LoginUserView(views.APIView):
  """Retrive and return authenticated user."""
  def post(self, request):
    """Verify, authenticate and return user."""
    email = request.data['email']
    password = request.data['password']
    scope = request.data['scope']

    user: User = User.objects().filter(email=email).first()

    if user is None:
      raise exceptions.AuthenticationFailed('User not found.')

    if not user.check_password(password):
      raise exceptions.AuthenticationFailed('Incorrect password.')

    token = JWTAuthentication.generate_jwt(user.id, scope)
    response = Response()
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
      'message': 'success'
    }

    return response


  class UserView(views.APIView):
    """Retrive and return user."""
    authentication_class = [JWTAuthentication]
    permission_class = [IsAuthenticated]

    def get(self, request):
      """Return user."""
      user = request.data
      data = UserSerializer(user).data

      return Response(data)
