from django.urls import path
# from .views import SensorDetail, ListCreateAPIView
from .serializers import SensorDetailSerializer
from .views import MesurementAPI, SingleSensorView, SensorView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    # path('sensors/', SensorAPI.as_view()),
    # path('sensors/<pk>/', SensorAPI.as_view()),
    path('measurements/', MesurementAPI.as_view()),
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', SingleSensorView.as_view()),



]
