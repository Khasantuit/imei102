from django.urls import path
from .views import *

urlpatterns = [
    # Jinoyat urls
    path('',JinoyatApiView.as_view()),
    path('create/',JinoyatApiCreate.as_view()),
    path('<int:pk>',JinoyatApiUpdate.as_view()),
]