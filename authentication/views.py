from rest_framework.generics import *
from authentication.models import *
from .serializers import *
# from rest_framework import permissions

# Test Api
class AuthApiView(ListAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Auth.objects.all()
    serializer_class = AuthSerializer
class AuthApiCreate(ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Auth.objects.all()
    serializer_class = AuthSerializer
class AuthApiUpdate(RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Auth.objects.all()
    serializer_class = AuthSerializer