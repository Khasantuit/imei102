from rest_framework.generics import *
from jinoyat.models import *
from .serializers import *
#from rest_framework import permissions

# Test Api
class JinoyatApiView(ListAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Jinoyat.objects.all()
    serializer_class = JinoyatSerializer
class JinoyatApiCreate(ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Jinoyat.objects.all()
    serializer_class = JinoyatSerializer
class JinoyatApiUpdate(RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Jinoyat.objects.all()
    serializer_class = JinoyatSerializer