from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from offline_business_analyzer.apps.account.views import registration_view

app_name = 'account'

urlpatterns = [
    path('register', registration_view, name='register-user'),
    path('login', obtain_auth_token, name='login'),
]
