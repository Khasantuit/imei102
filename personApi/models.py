from django.db import models

class Person(models.Model):
    fio = models.CharField(max_length=15, null=True)
    number = models.CharField(max_length=10, null=True)
    region = models.CharField(max_length=100, null=True)
    boshqarma = models.CharField(max_length=100, null=True)
    lavozim = models.CharField(max_length=100, null=True)
    unvon = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.title[:15]