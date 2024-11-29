from rest_framework import serializers
from tyj.models import *

class TYJSerializer(serializers.ModelSerializer):
    class Meta:
        model = TYJ
        fields = ('id', 'tyj_N','shartli_nom', 'info')