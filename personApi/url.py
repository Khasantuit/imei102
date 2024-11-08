from django.urls import path
from .views import *

urlpatterns = [
    # Person urls
    path('', PersonApiView.as_view()),
    path('create/', PersonApiCreate.as_view()),
    path('<int:pk>', PersonApiUpdate.as_view()),
]