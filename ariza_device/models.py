from django.db import models

class ArizaDevice(models.Model):
    imei = models.CharField(max_length=15, null=True)
    number = models.CharField(max_length=15, null=True)
    model = models.CharField(max_length=100, null=True)
    color = models.CharField(max_length=100, null=True)
    info = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.imei[:15]