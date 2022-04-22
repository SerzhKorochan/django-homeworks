from rest_framework import generics, status
from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, SensorListSerializer, MeasurementSerializer
from rest_framework.response import Response


class SensorView(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class SensorListView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorListSerializer


class MeasurementView(generics.CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
