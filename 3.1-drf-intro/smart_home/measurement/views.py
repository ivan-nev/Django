# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, \
    ListCreateAPIView

from rest_framework.response import Response

from .models import Sensor, Measurement
from .serializers import MeasurementSerializer, SensorDetailSerializer,SensorSimpleSerializer


class MesurementAPI(ListAPIView):
    """Добавить измерение. Указываются ID датчика и температура"""
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        review = MeasurementSerializer(data=request.data)
        if review.is_valid():
            review.save()
        return Response({'status': 'OK'})


class SingleSensorView(RetrieveUpdateAPIView):
    """Получение инф. по датчику, обновление имени и описания"""
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class SensorView(ListCreateAPIView):
    """Список датчиков, создание датчика"""
    queryset = Sensor.objects.all()
    serializer_class = SensorSimpleSerializer


