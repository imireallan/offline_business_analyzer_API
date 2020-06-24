from django.urls import path
from .views import upload_csv

app_name = 'business'

urlpatterns = [
    path('upload', upload_csv, name='upload_csv'),
]
