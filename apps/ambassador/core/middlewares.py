""" Manage middlewares. """


from ambassador.services import UserService


class AuthMiddleware:
  """Authentication middleware."""
  def __init__(self, get_response) -> None:
     self.get_response = get_response

  def __call__(self, request):
    try:
      user = UserService.get('', headers=request.headers)
    except:
      user = None

    request.user_ms = user

    return self.get_response(request)