from django.urls import path, include
from .views import *

app_name = 'api'

urlpatterns = [
    path('tank/<int:pk>/', TankAPIView.as_view(), name='tank'),
    path('tanks/', TankListAPIView.as_view(), name='tanks'),
]