from django.urls import path
from .views import *

urlpatterns = [
    # User urls
    path('', registrationView.as_view()),
    path('create/', registrationCreate.as_view()),
    path('<int:pk>', registrationUpdate.as_view()),
]