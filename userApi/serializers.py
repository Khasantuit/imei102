from rest_framework import serializers
from userApi.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'fio', 'number','jshshr','manzili', 'shakl1')