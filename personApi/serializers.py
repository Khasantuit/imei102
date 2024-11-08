from rest_framework import serializers
from personApi.models import *

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'fio', 'number','region','boshqarma', 'lavozim', 'unvon')