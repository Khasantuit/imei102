from rest_framework.generics import *
from pincode.models import *
from .serializers import *
# from rest_framework import permissions

# Test Api
class PinCodeApiView(ListAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Pin.objects.all()
    serializer_class = PinCodeSerializer
class PinCodeApiCreate(ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Pin.objects.all()
    serializer_class = PinCodeSerializer
class PinCodeApiUpdate(RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Pin.objects.all()
    serializer_class = PinCodeSerializer