from rest_framework import serializers
from registration.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'fio','region','boshqarma', 'lavozim', 'unvon')