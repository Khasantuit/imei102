from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('device/', include('deviceApi.url')),
    path('person/', include('personApi.url')),
    path('user/', include('userApi.url')),

]
