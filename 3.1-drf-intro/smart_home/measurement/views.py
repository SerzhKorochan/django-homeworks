from rest_framework import generics, status
from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, MeasurementSerializer
from rest_framework.response import Response


class SensorView(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def post(self, request):
        self.queryset.create(
            name = request.data.get('name', 'default'),
            description = request.data.get('description', 'default')
        )

        return Response(status=status.HTTP_201_CREATED)
