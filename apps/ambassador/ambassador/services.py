""" Services for ambassador app."""

import requests
import json

class UserService:
  endpoint = 'http://host.docker.internal:8003/api/user/'
  endpoint_users = 'http://host.docker.internal:8003/api/users/'

  @staticmethod
  def __generate_path(path: str, is_users_endpoint: bool = False):
    """Generate endpoint path."""
    url = UserService.endpoint
    if is_users_endpoint:
      url = UserService.endpoint_users

    if not path:
      return url

    return f'{url}{path}/'

  @staticmethod
  def get(path: str, **kwargs):
    """Send HTTP GET request."""
    headers = kwargs.get('headers', None)
    is_users_endpoint = kwargs.get('is_users_endpoint', False)
    return requests.get(
      UserService.__generate_path(path=path, is_users_endpoint=is_users_endpoint),
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
      data=json.dumps(data),
      headers=headers,
    ).json()
