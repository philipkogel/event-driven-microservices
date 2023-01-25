""" Services for ambassador app."""

import requests


class UserService:
  endpoint = 'http://host.docker.internal:8003/api/user/'

  @staticmethod
  def __generate_path(path: str):
    """Generate endpoint path."""
    if not path:
      return UserService.endpoint

    return f'{UserService.endpoint}{path}/'

  @staticmethod
  def get(path: str, **kwargs):
    """Send HTTP GET request."""
    headers = kwargs.get('headers', None)
    return requests.get(
      UserService.__generate_path(path=path),
      headers=headers
    ).json()

  @staticmethod
  def post(path: str, **kwargs):
    """Send HTTP POST request."""
    headers = kwargs.get('headers', None)
    data = kwargs.get('data', None)
    return requests.post(
      UserService.__generate_path(path=path),
      data=data,
      headers=headers,
    ).json()

  @staticmethod
  def put(path: str, **kwargs):
    """Send HTTP PUT request."""
    headers = kwargs.get('headers', None)
    data = kwargs.get('data', None)
    return requests.put(
      UserService.__generate_path(path=path),
      data=data,
      headers=headers,
    ).json()
