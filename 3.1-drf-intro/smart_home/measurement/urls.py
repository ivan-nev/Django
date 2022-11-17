from django.urls import path
# from .views import SensorDetail, ListCreateAPIView
from .views import  MesurementAPI, SensorAPI

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorAPI.as_view()),
    path('sensors/<pk>/', SensorAPI.as_view()),
    path('measurements/', MesurementAPI.as_view()),



]
