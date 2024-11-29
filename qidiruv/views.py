from rest_framework.generics import *
from qidiruv.models import *
from .serializers import *
#from rest_framework import permissions

# Test Api
class QidiruvApiView(ListAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Qidiruv.objects.all()
    serializer_class = QidiruvSerializer
class QidiruvApiCreate(ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Qidiruv.objects.all()
    serializer_class = QidiruvSerializer
class QidiruvApiUpdate(RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Qidiruv.objects.all()
    serializer_class = QidiruvSerializer