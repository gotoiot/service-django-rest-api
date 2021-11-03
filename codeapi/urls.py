"""codeapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from dj_rest_auth.registration.views import VerifyEmailView, ConfirmEmailView
from dj_rest_auth.views import PasswordResetConfirmView

from codeapi.views import app_home


urlpatterns = [

    # the panel for the admin site 
    path('admin/', admin.site.urls),
    
    # path to each installed application
    path('v1/assesments/', include('assesments.urls', namespace="assesments")),
    
    # All packages needed for the next features: user registration, login,
    # logout, password reset, profile, email account activation, and more.
    # Go to all-auth and dj-rest-auth to check specific settings.
    # Note: the account confirm email view must be before any other dj-rest-auth view
    path('auth/registration/account-confirm-email/<str:key>/', ConfirmEmailView.as_view()),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('auth/account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    path('auth/password/reset/confirm/<slug:uidb64>/<slug:token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    
    # the whole application home is loaded once all views are loaded
    path('', app_home, name='app-home'),
]
