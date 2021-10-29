from rest_framework import generics, permissions, renderers, status

from users.models import ApiUser
from users.serializers import ApiUserSerializer


class UserDetail(generics.RetrieveAPIView):
    """
    From this endpoint you can get the details of instances created.
    """
    queryset = ApiUser.objects.all()
    serializer_class = ApiUserSerializer