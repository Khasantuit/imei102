from rest_framework.generics import *
from userApi.models import *
from .serializers import *
#from rest_framework import permissions

# Device Api
class UserApiView(ListAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
class UserApiCreate(ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
class UserApiUpdate(RetrieveUpdateDestroyAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer