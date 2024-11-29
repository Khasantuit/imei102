from django.urls import path
from .views import *

urlpatterns = [
    # Auth urls
    path('',AuthApiView.as_view()),
    path('create/',AuthApiCreate.as_view()),
    path('<int:pk>',AuthApiUpdate.as_view()),
]