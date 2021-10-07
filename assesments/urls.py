from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from assesments import views

app_name = 'assesments'

urlpatterns = [
    path('', views.api_root, name='assesments-home'),
    path('assesments/', views.AssesmentList.as_view(), name='assesment-list'),
    path('assesments/<int:pk>/', views.AssesmentDetail.as_view(), name='assesment-detail'),
    path('instances/', views.InstanceList.as_view(), name='instance-list'),
    path('instances/<uuid:pk>/', views.InstanceDetail.as_view(), name="instance-detail"),
    path('takers/', views.TakerList.as_view(), name='taker-list'),
    path('takers/<int:pk>/', views.TakerDetail.as_view(), name="taker-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)