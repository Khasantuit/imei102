from rest_framework.generics import *
from ariza_device.models import *
from .serializers import *
#from rest_framework import permissions

# Device Api
class ArizaDeviceApiView(ListAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = ArizaDevice.objects.all()
    serializer_class = ArizaDeviceSerializer
class ArizaDeviceApiCreate(ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = ArizaDevice.objects.all()
    serializer_class = ArizaDeviceSerializer
class ArizaDeviceApiUpdate(RetrieveUpdateDestroyAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = ArizaDevice.objects.all()
    serializer_class = ArizaDeviceSerializer