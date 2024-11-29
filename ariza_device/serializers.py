from rest_framework import serializers
from ariza_device.models import *

class ArizaDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArizaDevice
        fields = ('id', 'imei','number','model', 'color', 'info')