from rest_framework.generics import *
from login.models import *
from .serializers import *
# from rest_framework import permissions

# Login Api
class LoginApiView(ListAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Login.objects.all()
    serializer_class = LoginSerializer
class LoginApiCreate(ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Login.objects.all()
    serializer_class = LoginSerializer
class LoginApiUpdate(RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Login.objects.all()
    serializer_class = LoginSerializer