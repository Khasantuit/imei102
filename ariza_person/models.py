from django.db import models

class DevicePerson(models.Model):
    fio = models.CharField(max_length=100, null=True)
    number = models.CharField(max_length=100, null=True)
    jshshr = models.CharField(max_length=100, null=True)
    shakl1 = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.jshshr[:15]