from rest_framework import serializers
from deviceApi.models import *

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('id', 'imei','number','model', 'color', 'info')