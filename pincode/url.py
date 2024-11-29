from django.urls import path
from .views import *

urlpatterns = [
    # Test urls
    path('',PinCodeApiView.as_view()),
    path('create/',PinCodeApiCreate.as_view()),
    path('<int:pk>',PinCodeApiUpdate.as_view()),
]