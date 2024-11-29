from rest_framework import serializers
from jinoyat.models import *

class JinoyatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jinoyat
        fields = ('id', 'jinoyat_N', 'fio', 'jshshir', 'info', 'number')