from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ariza_device/', include('api.ariza_device.url')),
    path('ariza_person/', include('api.ariza_person.url')),
    path('registration/', include('api.registration.url')),
    path('jinoyat/', include('api.jinoyat.url')),
    path('tyj/', include('api.tyj.url')),
    path('pincode/', include('api.pincode.url')),
    path('auth/', include('api.authentication.url')),

]