from django.db import models

class User(models.Model):
    fio = models.CharField(max_length=15, null=True)
    number = models.CharField(max_length=10, null=True)
    jshshr = models.CharField(max_length=100, null=True)
    manzili = models.CharField(max_length=100, null=True)
    shakl1 = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.title[:15]