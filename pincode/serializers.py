from rest_framework import serializers
from pincode.models import *

class PinCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pin
        fields = ('id', 'code')