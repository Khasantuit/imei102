from rest_framework import serializers
from login.models import *

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ('id', 'number','jeton_N')