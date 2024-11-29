from django.urls import path
from .views import *

urlpatterns = [
    # Login urls
    path('',LoginApiView.as_view()),
    path('create/',LoginApiCreate.as_view()),
    path('<int:pk>',LoginApiUpdate.as_view()),
]