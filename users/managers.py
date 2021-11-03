from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class ApiUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        This func automatically creates EmailAddress entry in a safety way.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        
        user = self.create_user(email, password, **extra_fields)
        # creates an EmailAddress (for allauth) entry with user data
        ApiUserManager.create_email_address_entry(user, True, True)
        return user

    @classmethod
    def create_email_address_entry(cls, user, verified, primary):
        # Tries to create an EmailAddress entry when calling createsuperuser command
        # TODO try to import the model from a settings field in the settings.py
        try:
            from allauth.account.models import EmailAddress
            EmailAddress.objects.create(user=user, email=user.email, verified=verified, primary=primary)
        except:
            print("Superuser has not been added to EmailAddress all-auth table. Add it manually please!")
