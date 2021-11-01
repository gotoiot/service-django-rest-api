from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from assesments import views

app_name = 'assesments'

urlpatterns = [
    path('', views.api_root, name='assesments-home'),
    path('assesments/', views.AssesmentList.as_view(), name='assesment-list'),
    path('assesments/<int:pk>/', views.AssesmentDetail.as_view(), name='assesment-detail'),
    path('assesments/<int:pk>/status', views.AssesmentStatus.as_view(), name='assesment-status'),
    path('assesments/<int:pk>/create', views.InstanceCreate.as_view(), name='instance-creation'),
    path('instances/', views.InstanceList.as_view(), name='instance-list'),
    path('instances/<uuid:pk>/', views.InstanceDetail.as_view(), name="instance-detail"),
    path('instances/<uuid:pk>/test', views.InstanceTest.as_view(), name="instance-test"),
    path('instances/<uuid:pk>/start', views.InstanceStart.as_view(), name="instance-start"),
    path('instances/<uuid:pk>/questions/<int:q_id>', views.InstanceQuestionDetail.as_view(), name="instance-question-detail"),
    path('instances/<uuid:pk>/answer', views.InstanceAnswer.as_view(), name="instance-answer"),
    path('instances/<uuid:pk>/end', views.InstanceEnd.as_view(), name="instance-end"),
    path('instances/<uuid:pk>/result', views.InstanceResult.as_view(), name="instance-result"),
    path('instances/restore', views.InstanceRestore.as_view(), name="instance-restore"),
    path('takers/', views.TakerList.as_view(), name='taker-list'),
    path('takers/<int:pk>/', views.TakerDetail.as_view(), name="taker-detail"),
    path('takers/me', views.TakerDetailMeAnswer.as_view(), name='taker-detail-me'),
    path('questions/', views.QuestionList.as_view(), name='question-list'),
    path('questions/<int:pk>/', views.QuestionDetail.as_view(), name='question-detail'),
    path('options/', views.OptionList.as_view(), name='option-list'),
    path('options/<int:pk>/', views.OptionDetail.as_view(), name='option-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)