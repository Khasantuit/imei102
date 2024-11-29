from django.urls import path
from .views import *

urlpatterns = [
    # DevicePerson urls
    path('', DevicePersonApiView.as_view()),
    path('create/', DevicePersonApiCreate.as_view()),
    path('<int:pk>', DevicePersonApiUpdate.as_view()),
]