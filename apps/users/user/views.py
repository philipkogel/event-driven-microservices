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
    user = User.objects.filter(email=email).first()

    if user is None:
      raise exceptions.AuthenticationFailed('User not found.')

    if not user.check_password(password):
      raise exceptions.AuthenticationFailed('Incorrect password.')

    token = JWTAuthentication.generate_jwt(user.id, scope)
    JWTAuthentication.create_user_token(
      user_id=user.id,
      token=token
    )

    return Response({
      'jwt': token,
    })


class BaseUserAuthenticatedView(views.APIView):
    """Base User View."""
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class UserView(BaseUserAuthenticatedView):
    """Retrive and return user."""

    def get(self, request):
      """Return user."""
      return Response(UserSerializer(request.user).data)

class UserLogoutView(BaseUserAuthenticatedView):
  """Manage user logout."""

  def post(self, request):
    """Handle user logout."""
    print(request.user)
    JWTAuthentication.delete_token(user_id=request.user.id)

    return Response({
      'message': 'success'
    })


class UserProfileInfoView(BaseUserAuthenticatedView):
  """View for user profile info update."""

  def put(self, request, pk=None):
    """User profile info update"""
    user = request.data
    serializer = UserSerializer(user, data=user, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(serializer.data)


class UserPasswordView(BaseUserAuthenticatedView):
  """View for user password update."""

  def put(self, request, pk=None):
    """User password update."""
    user = request.user
    data = request.data

    if data['password'] != data['password_confirm']:
      raise exceptions.APIException('Passwords do not match')

    user.set_password(data['password'])
    user.save()

    return Response(UserSerializer(user).data)

