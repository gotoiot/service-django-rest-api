from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from assesments import views

app_name = 'assesments'

urlpatterns = [
]

urlpatterns = format_suffix_patterns(urlpatterns)