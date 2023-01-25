import jwt, datetime
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
from django.db.models import ProtectedError
from app import settings
from core.models import User, UserToken


class JWTAuthentication(BaseAuthentication):
  """User authentication class."""
  def authenticate(self, request):
    token = request.COOKIES.get('jwt')

    if not token:
      return None

    try:
      payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
      raise exceptions.AuthenticationFailed('Unauthenticated')

    user = User.objects.get(pk=payload['user_id'])

    if user is None:
      raise exceptions.AuthenticationFailed('User not found!')

    if not UserToken.objects.filter(
        user_id=user.id,
        token=token,
        expired_at__gt=datetime.datetime.utcnow()
      ).exists():
      raise exceptions.AuthenticationFailed('Unauthenticated')


    return (user, None)

  @staticmethod
  def generate_jwt(id, scope):
    """Generate and return JWT Token."""
    payload = {
      'user_id': id,
      'scope': scope,
      'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
      'iat': datetime.datetime.utcnow()
    }

    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')


  @staticmethod
  def create_user_token(user_id: str, token: str) -> None:
    """Create user token."""
    UserToken.objects.create(
      user_id=user_id,
      token=token,
      created_at=datetime.datetime.utcnow(),
      expired_at=datetime.datetime.utcnow() + datetime.timedelta(days=1)
    )

  @staticmethod
  def delete_token(user_id: str) -> None:
    """Delete user token."""
    print(user_id)
    try:
      UserToken.objects.filter(user_id=user_id).delete()
    except ProtectedError:
      raise exceptions.PermissionDenied('Unable to delete token.')

