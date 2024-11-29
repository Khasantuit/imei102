from rest_framework import serializers
from jinoyat.models import *

class JinoyatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jinoyat
        fields = ('id', 'jinoyatn','number','fio', 'jshshir', 'info')