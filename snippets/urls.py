from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

app_name = 'snippets'

urlpatterns = [
    path('', views.SnippetList.as_view(), name='snippets'),
    path('<int:pk>/', views.SnippetDetail.as_view(), name='snippet_detail'),
    path('users/', views.UserList.as_view(), name='users'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name="user_detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)