from rest_framework import serializers
from ariza_person.models import *

class DevicePersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevicePerson
        fields = ('id', 'fio', 'number','jshshr', 'shakl1')