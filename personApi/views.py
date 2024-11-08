from rest_framework.generics import *
from personApi.models import *
from .serializers import *
#from rest_framework import permissions

# Device Api
class PersonApiView(ListAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
class PersonApiCreate(ListCreateAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
class PersonApiUpdate(RetrieveUpdateDestroyAPIView):
    #permission_classes = (permissions.IsAuthenticated,)
    queryset = Person.objects.all()
    serializer_class = PersonSerializer