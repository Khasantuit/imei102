from django.urls import path
from .views import *

urlpatterns = [
    # ArizaDevice urls
    path('',ArizaDeviceApiView.as_view()),
    path('create/',ArizaDeviceApiCreate.as_view()),
    path('<int:pk>',ArizaDeviceApiUpdate.as_view()),
]