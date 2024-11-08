from django.urls import path
from .views import *

urlpatterns = [
    # User urls
    path('', UserApiView.as_view()),
    path('create/', UserApiCreate.as_view()),
    path('<int:pk>', UserApiUpdate.as_view()),
]