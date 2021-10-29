from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from users.managers import CustomUserManager

# TODO try to get this model working with all-auth in rest-auth 

class ApiUser(AbstractUser):
    # username = None
    # email = models.EmailField(_('email address'), unique=True)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = []

    # objects = CustomUserManager()

    def __str__(self):
        return self.email