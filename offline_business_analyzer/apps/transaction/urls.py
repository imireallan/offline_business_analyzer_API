from django.urls import path
from .views import uploadCSV

app_name = 'business'

urlpatterns = [
    path('upload', uploadCSV, name='upload_csv'),
]
