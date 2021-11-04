from rest_framework import status
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework.decorators import api_view
from django.urls import path, include


@api_view(['GET'])
# @permission_classes([permissions.IsAuthenticated | permissions.IsAdminUser])
def app_home(request, format=None):
    """
    This is the main application endpoint.
    From this endpoint you can explore each resources by clicking in each link below.
    """
    response = {
        'assesments_home': reverse('assesments:assesments-home', request=request, format=format),
        'assesments_my_profile': reverse('assesments:taker-detail-me', request=request, format=format),
        'assesments_my_instances': reverse('assesments:instance-list', request=request, format=format),
        'assesments_list': reverse('assesments:assesment-list', request=request, format=format),
        'login': reverse('rest_login', request=request, format=format),
        'logout': reverse('rest_logout', request=request, format=format),
        'password_change': reverse('rest_password_change', request=request, format=format),
        'register': reverse('rest_register', request=request, format=format),
    }
    return Response(response, status=status.HTTP_200_OK)

