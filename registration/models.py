from django.db import models

class User(models.Model):
    fio = models.CharField(max_length=100, null=True)
    region = models.CharField(max_length=100, null=True)
    boshqarma = models.CharField(max_length=100, null=True)
    lavozim = models.CharField(max_length=100, null=True)
    unvon = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.fio[:100]