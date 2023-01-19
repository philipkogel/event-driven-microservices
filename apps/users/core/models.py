from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
  def create_user(self, email: str, password: str = None, **extra_fields):
    """Create save and return a new user."""
    if not email:
      raise ValueError("User must have an email!")
    if not password:
      raise ValueError("User must have an password!")

    user = self.model(
      email=self.normalize_email(email),
      **extra_fields
    )
    user.set_password(password)
    user.is_admin=False
    user.is_staff=False
    user.is_ambassador=False
    user.save(using=self.db)

    return user

  def create_superuser(self, email: str, password: str = None):
    """Create and return a new superuser."""
    user = self.create_user(email=email, password=password)
    user.is_admin = True
    user.is_staff = True
    user.is_ambassador = True
    user.is_superuser = True
    user.save(using=self.db)

    return user

class User(AbstractUser):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.EmailField(max_length=255, unique=True)
  password = models.CharField(max_length=255)
  is_ambassador = models.BooleanField(default=True)
  username = None

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  objects = UserManager()

  @property
  def name(self):
    """Return users full name"""
    return f"{self.first_name} {self.last_name}"

  # @property
  # def revenue(self):
  #   """Return users revenue"""
  #   orders =
