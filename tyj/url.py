from django.urls import path
from .views import *

urlpatterns = [
    # TYJ urls
    path('',TYJApiView.as_view()),
    path('create/',TYJApiCreate.as_view()),
    path('<int:pk>',TYJApiUpdate.as_view()),
]