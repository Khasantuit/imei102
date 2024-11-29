from django.db import models

class TYJ(models.Model):
    tyjn = models.CharField(max_length=200, null=True)
    shartli_nom = models.CharField(max_length=200, null=True)
    info = models.CharField(max_length=200, null=True)
    number = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.tyj[:10]