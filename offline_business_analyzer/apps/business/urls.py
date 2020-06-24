from django.urls import path
from .views import RegisterBusiness, BusinessRUDView, BusinessListView, retrieve_business_by_owner

app_name = 'business'

urlpatterns = [
    path('register', RegisterBusiness.as_view(), name='register-business'),
    path('detail/<name>', BusinessRUDView.as_view(), name='business-detail'),
    path('owner', retrieve_business_by_owner, name='business-owner'),
    path('list', BusinessListView.as_view(), name='business-list'),
]
