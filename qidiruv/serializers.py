from rest_framework import serializers
from qidiruv.models import *

class QidiruvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qidiruv
        fields = ('id', 'qidiruv_N', 'fio', 'jshshir', 'info', 'number')