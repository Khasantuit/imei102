from rest_framework import serializers
from authentication.models import *

class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auth
        fields = ('id', 'number','JetonN')