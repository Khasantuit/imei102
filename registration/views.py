from rest_framework.generics import *
from registration.models import *
from .serializers import *
#from rest_framework import permissions

# Test Api
class registrationView(ListAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
class registrationCreate(ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
class registrationUpdate(RetrieveUpdateDestroyAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer