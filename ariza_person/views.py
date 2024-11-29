from rest_framework.generics import *
from ariza_person.models import *
from .serializers import *
#from rest_framework import permissions

# DevicePerson Api
class DevicePersonApiView(ListAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = DevicePerson.objects.all()
    serializer_class = DevicePersonSerializer
class DevicePersonApiCreate(ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = DevicePerson.objects.all()
    serializer_class = DevicePersonSerializer
class DevicePersonApiUpdate(RetrieveUpdateDestroyAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = DevicePerson.objects.all()
    serializer_class = DevicePersonSerializer