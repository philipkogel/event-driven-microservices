"""
Serializers for the User API view.
"""

from django.contrib.auth import (
  get_user_model,
  authenticate
)
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
  """User object serializer."""
  class Meta:
    model = get_user_model()
    fields = ['id', 'first_name', 'last_name', 'email', 'password', 'is_ambassador']
    extra_kwargs = {
      'password': {
        'write_only': True,
        'min_length': 5,
      }
    }

  def create(self, validated_data):
    """Create and return user with encrypted password."""
    password = validated_data.pop('password', None)
    user = self.Meta.model(**validated_data)
    if password is not None:
      user.set_password(password)

    user.save()

    return user


class UserInfoSerializer(serializers.ModelSerializer):
  """User Info object serializer."""
  class Meta:
    model = get_user_model()
    fields = ['id', 'first_name', 'last_name', 'email', 'is_ambassador']
    read_only_fields = ['id', 'is_ambassador']

    def update(self, instance, validated_data):
      """Update and return user."""
      return super().update(instance, validated_data)


class UserPasswordUpdateSerializer(serializers.Serializer):
  """User Password object serializer."""
  password = serializers.CharField()
  password_confirm = serializers.CharField()