# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from .models import Sensor, Measurement
from .serializers import MeasurementSerializer, SensorDetailSerializer,SensorSimpleSerializer


class SensorAPI(ListAPIView):
    """Получить список датчиков. Выдается список с краткой информацией по датчикам:
    ID, название и описание"""
    queryset = Sensor.objects.all()
    serializer_class = SensorSimpleSerializer

    # def get(self, request):
    #     pk = (request.GET.get('pk'))
    #
    #     if pk is not None:
    #         queryset = Sensor.objects.all()
    #         serializer_class = SensorDetailSerializer
    #     else:
    #         queryset = Sensor.objects.all()
    #         serializer_class = SensorSimpleSerializer



    """Создание датчика"""
    def post(self, request):
        queryset = Sensor.objects.all()
        serializer_class = SensorDetailSerializer
        review = SensorDetailSerializer(data=request.data)
        if review.is_valid():
            review.save()
        return Response({'status': 'OK'})

    def patch(self, request, pk):
        """Изменить датчик. Указываются название и/или описание."""
        queryset = Sensor.objects.all()
        serializer_class = SensorDetailSerializer
        sensor = Sensor.objects.get(pk=pk)
        serializer = SensorDetailSerializer(sensor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)


class MesurementAPI(ListAPIView):
    """Добавить измерение. Указываются ID датчика и температура"""
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        review = MeasurementSerializer(data=request.data)
        if review.is_valid():
            review.save()
        return Response({'status': 'OK'})