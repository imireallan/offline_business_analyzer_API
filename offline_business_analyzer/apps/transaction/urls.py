from django.urls import path
from .views import uploadCSV, UploadCSV

app_name = 'business'

urlpatterns = [
    path('upload', uploadCSV, name='upload_csv'),
    path('upload-file', UploadCSV.as_view(), name='upload_csv'),
]
