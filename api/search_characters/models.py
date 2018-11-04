from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.core.validators import int_list_validator


class UserManager(BaseUserManager):
    """Helps Django create a custom user"""

    def create_user(self, email, name, password=None):
        """Creates a new User"""
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        # set_password hashes pw
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Creates and saves a new superuser"""

        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class SearchIndex(models.Model):
    """Many Users can share the same SearchIndex"""
    name = models.CharField(max_length=255, unique=True)

class User(AbstractBaseUser, PermissionsMixin):
    """User has many index permissions"""

    index_list = models.ManyToManyField(SearchIndex)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email
