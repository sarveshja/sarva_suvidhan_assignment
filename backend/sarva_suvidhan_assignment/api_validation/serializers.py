from rest_framework import serializers
from .models import *

class IcfWheelMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = IcfWheelMeasurement
        fields = '__all__'

class IcfBogieChecksheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = IcfBogieChecksheet
        fields = '__all__'