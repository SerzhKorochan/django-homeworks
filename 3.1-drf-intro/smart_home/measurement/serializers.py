from rest_framework import serializers
from .models import Measurement, Sensor


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at', 'sensor']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(many = True, read_only = True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']


class SensorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']
