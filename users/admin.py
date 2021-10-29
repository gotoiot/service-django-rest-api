from django.contrib import admin

from users.models import ApiUser

# TODO create a class to manage this model in the admin

admin.site.register(ApiUser)
