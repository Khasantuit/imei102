from rest_framework.generics import *
from tyj.models import *
from .serializers import *
#from rest_framework import permissions

# Test Api
class TYJApiView(ListAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = TYJ.objects.all()
    serializer_class = TYJSerializer
class TYJApiCreate(ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = TYJ.objects.all()
    serializer_class = TYJSerializer
class TYJApiUpdate(RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = TYJ.objects.all()
    serializer_class = TYJSerializer