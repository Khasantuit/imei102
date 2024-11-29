from rest_framework import serializers
from tyj.models import *

class TYJSerializer(serializers.ModelSerializer):
    class Meta:
        model = TYJ
        fields = ('id', 'tyjn','shartli_nom', 'info')