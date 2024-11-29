from django.db import models

class Jinoyat(models.Model):
    jinoyatn = models.CharField(max_length=200, null=True)
    number = models.CharField(max_length=100, null=True)
    fio = models.CharField(max_length=200, null=True)
    jshshir = models.CharField(max_length=200, null=True)
    info = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.jinoyatn[:10]