from django.urls import path
from .views import *

urlpatterns = [
    # Qidiruv urls
    path('',QidiruvApiView.as_view()),
    path('create/',QidiruvApiCreate.as_view()),
    path('<int:pk>',QidiruvApiUpdate.as_view()),
]