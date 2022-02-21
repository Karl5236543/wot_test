from django.urls import path
from .views import *

app_name='main_app'
urlpatterns = [
    # path('api/tank/<int:pk>/', api_tank_get, name='api_tank_get'),
    # path('api/tank/', api_tank_create, name='api_tank_create'),
    path('api/tank/<int:pk>/', TankRetriveUpdateAPIView.as_view(), name='api_tank'),
    path('api/tanks/', TankListAPIView.as_view(), name='api_tank'),
    path('', index, name='index'),
    path('2/', index2, name='index2'),
    path('create_tank/', CreateTank.as_view(), name='create_tank'),
    path('create_tank_2/', CreateTankView2.as_view(), name='create_tank_2'),
    path('create_tank_properties/', CreateTankPropertiesView.as_view(), name='create_tank_properties')
]