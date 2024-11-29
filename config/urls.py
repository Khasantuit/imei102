from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ariza_device/', include('ariza_device.url')),
    path('ariza_person/', include('ariza_person.url')),
    path('registration/', include('registration.url')),
    path('jinoyat/', include('jinoyat.url')),
    path('qidiruv/', include('qidiruv.url')),
    path('tyj/', include('tyj.url')),
    path('pincode/', include('pincode.url')),
    path('auth/', include('authentication.url')),

]