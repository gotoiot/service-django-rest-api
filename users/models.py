from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from users.managers import ApiUserManager


class ApiUser(AbstractUser):
    username = None
    first_name = None
    last_name = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = ApiUserManager()

    def __str__(self):
        return self.email